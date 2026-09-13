(() => {
  const container = document.getElementById('impactGraph');
  if (!container) return;

  const graphData = JSON.parse(document.getElementById('graphData')?.textContent || '{}');
  const impactData = JSON.parse(document.getElementById('impactData')?.textContent || 'null');
  const inspector = document.getElementById('nodeInspector');
  const toggleButton = document.getElementById('toggleImpact');
  const fitButton = document.getElementById('fitGraph');

  const components = graphData.components || [];
  const dependencies = graphData.dependencies || [];
  const componentById = new Map(components.map(c => [c.id, c]));
  const impactById = new Map((impactData?.impacts || []).map(item => [item.component, item]));
  const rootId = impactData?.root?.id || null;
  const impactedIds = new Set([rootId, ...impactById.keys()].filter(Boolean));

  const statusFor = id => {
    if (id === rootId) return 'root';
    const impact = impactById.get(id);
    if (!impact) return 'normal';
    return impact.depth === 1 ? 'direct' : 'indirect';
  };

  const SVG_NS = 'http://www.w3.org/2000/svg';
  const svg = document.createElementNS(SVG_NS, 'svg');
  svg.setAttribute('viewBox', '0 0 1100 640');
  svg.setAttribute('class', 'impact-svg');
  svg.setAttribute('aria-label', 'Grafo visual de dependencias de la aplicacion');
  svg.setAttribute('role', 'img');

  const defs = document.createElementNS(SVG_NS, 'defs');
  defs.innerHTML = `
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"></path>
    </marker>
    <filter id="glow"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  `;
  svg.appendChild(defs);

  const edgeLayer = document.createElementNS(SVG_NS, 'g');
  edgeLayer.setAttribute('class', 'edge-layer');
  const nodeLayer = document.createElementNS(SVG_NS, 'g');
  nodeLayer.setAttribute('class', 'node-layer');
  svg.append(edgeLayer, nodeLayer);

  const layout = buildLayout(components);
  dependencies.forEach((dep, index) => drawEdge(dep, index));
  components.forEach(drawNode);
  container.replaceChildren(svg);

  function buildLayout(items) {
    const positions = new Map();
    const cx = 540, cy = 320;
    const root = rootId ? items.find(c => c.id === rootId) : null;
    if (root) positions.set(root.id, {x: cx, y: cy});

    const impacted = items.filter(c => c.id !== rootId && impactedIds.has(c.id));
    const unaffected = items.filter(c => !impactedIds.has(c.id));

    impacted.sort((a, b) => (impactById.get(a.id)?.depth || 0) - (impactById.get(b.id)?.depth || 0));
    impacted.forEach((item, i) => {
      const depth = impactById.get(item.id)?.depth || 1;
      const sameDepth = impacted.filter(c => (impactById.get(c.id)?.depth || 1) === depth);
      const posInDepth = sameDepth.findIndex(c => c.id === item.id);
      const radius = 155 + (depth - 1) * 120;
      const start = -Math.PI / 2;
      const angle = start + ((posInDepth + 1) / (sameDepth.length + 1)) * Math.PI * 2;
      positions.set(item.id, {x: cx + Math.cos(angle) * radius, y: cy + Math.sin(angle) * radius});
    });

    unaffected.forEach((item, i) => {
      const radius = 270;
      const angle = (i / Math.max(unaffected.length, 1)) * Math.PI * 2;
      if (!positions.has(item.id)) positions.set(item.id, {x: cx + Math.cos(angle) * radius, y: cy + Math.sin(angle) * radius});
    });

    if (!root) {
      items.forEach((item, i) => {
        const radius = 245;
        const angle = (i / Math.max(items.length, 1)) * Math.PI * 2 - Math.PI / 2;
        positions.set(item.id, {x: cx + Math.cos(angle) * radius, y: cy + Math.sin(angle) * radius});
      });
    }
    return positions;
  }

  function drawEdge(dep, index) {
    const source = layout.get(dep.source);
    const target = layout.get(dep.target);
    if (!source || !target) return;

    const group = document.createElementNS(SVG_NS, 'g');
    const onImpact = impactedIds.has(dep.source) && impactedIds.has(dep.target);
    group.setAttribute('class', `graph-edge ${dep.documented ? 'documented' : 'hidden'} ${onImpact ? 'impact-edge' : ''}`);
    group.dataset.index = index;

    const line = document.createElementNS(SVG_NS, 'line');
    line.setAttribute('x1', source.x); line.setAttribute('y1', source.y);
    line.setAttribute('x2', target.x); line.setAttribute('y2', target.y);
    line.setAttribute('marker-end', 'url(#arrow)');
    line.setAttribute('vector-effect', 'non-scaling-stroke');

    const label = document.createElementNS(SVG_NS, 'text');
    label.setAttribute('x', (source.x + target.x) / 2);
    label.setAttribute('y', (source.y + target.y) / 2 - 7);
    label.setAttribute('text-anchor', 'middle');
    label.textContent = dep.kind;

    group.append(line, label);
    edgeLayer.appendChild(group);
  }

  function drawNode(component) {
    const p = layout.get(component.id);
    if (!p) return;
    const status = statusFor(component.id);
    const impact = impactById.get(component.id);
    const group = document.createElementNS(SVG_NS, 'g');
    group.setAttribute('class', `graph-node ${status}`);
    group.setAttribute('transform', `translate(${p.x} ${p.y})`);
    group.dataset.id = component.id;
    group.setAttribute('tabindex', '0');
    group.setAttribute('role', 'button');
    group.setAttribute('aria-label', `${component.name}, ${status}`);

    const circle = document.createElementNS(SVG_NS, 'circle');
    circle.setAttribute('r', status === 'root' ? '54' : '45');
    if (status === 'root') circle.setAttribute('filter', 'url(#glow)');

    const title = document.createElementNS(SVG_NS, 'text');
    title.setAttribute('class', 'node-title');
    title.setAttribute('text-anchor', 'middle');
    wrapSvgText(title, component.name, 15);

    const meta = document.createElementNS(SVG_NS, 'text');
    meta.setAttribute('class', 'node-meta');
    meta.setAttribute('text-anchor', 'middle');
    meta.setAttribute('y', '30');
    meta.textContent = status === 'root' ? 'ROOT' : impact ? `L${impact.depth}` : component.kind;

    group.append(circle, title, meta);
    group.addEventListener('click', () => updateInspector(component, status, impact));
    group.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') updateInspector(component, status, impact); });
    nodeLayer.appendChild(group);
  }

  function wrapSvgText(textNode, label, maxChars) {
    const words = label.split(/\s+/);
    const lines = [];
    let current = '';
    words.forEach(word => {
      const next = current ? `${current} ${word}` : word;
      if (next.length > maxChars && current) { lines.push(current); current = word; } else current = next;
    });
    if (current) lines.push(current);
    const offset = -((lines.length - 1) * 8);
    lines.forEach((line, i) => {
      const tspan = document.createElementNS(SVG_NS, 'tspan');
      tspan.setAttribute('x', '0');
      tspan.setAttribute('dy', i === 0 ? String(offset) : '16');
      tspan.textContent = line;
      textNode.appendChild(tspan);
    });
  }

  function updateInspector(component, status, impact) {
    const labels = {root: 'Cambio raiz', direct: 'Impacto directo', indirect: 'Impacto indirecto', normal: 'No impactado'};
    inspector.innerHTML = `
      <span class="eyebrow">Inspector</span>
      <h3>${escapeHtml(component.name)}</h3>
      <div class="inspector-badge ${status}">${labels[status]}</div>
      <dl>
        <div><dt>Tipo</dt><dd>${escapeHtml(component.kind)}</dd></div>
        <div><dt>Criticidad</dt><dd>C${component.criticality}</dd></div>
        <div><dt>Owner</dt><dd>${escapeHtml(component.owner)}</dd></div>
        ${impact ? `<div><dt>Nivel</dt><dd>L${impact.depth}</dd></div>` : ''}
      </dl>
      ${impact?.validation ? `<p><strong>Validacion:</strong><br>${escapeHtml(impact.validation)}</p>` : ''}
    `;
  }

  function escapeHtml(value) {
    return String(value ?? '').replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
  }

  let impactOnly = false;
  toggleButton?.addEventListener('click', () => {
    impactOnly = !impactOnly;
    [...svg.querySelectorAll('.graph-node')].forEach(node => {
      node.classList.toggle('dimmed', impactOnly && !impactedIds.has(node.dataset.id));
    });
    [...svg.querySelectorAll('.graph-edge')].forEach(edge => {
      edge.classList.toggle('dimmed', impactOnly && !edge.classList.contains('impact-edge'));
    });
    toggleButton.textContent = impactOnly ? 'Ver ecosistema' : 'Solo impacto';
  });

  fitButton?.addEventListener('click', () => {
    svg.setAttribute('viewBox', '0 0 1100 640');
  });

  if (rootId && componentById.has(rootId)) updateInspector(componentById.get(rootId), 'root', null);
})();
