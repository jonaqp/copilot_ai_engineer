(() => {
  const container = document.getElementById('impactGraph');
  if (!container) return;

  const graphData = JSON.parse(document.getElementById('graphData').textContent || '{}');
  const impactData = JSON.parse(document.getElementById('impactData').textContent || 'null');
  const inspector = document.getElementById('nodeInspector');
  const toggleButton = document.getElementById('toggleImpact');
  const fitButton = document.getElementById('fitGraph');

  const impactById = new Map((impactData?.impacts || []).map(item => [item.component, item]));
  const rootId = impactData?.root?.id || null;
  const impactedIds = new Set([rootId, ...impactById.keys()].filter(Boolean));

  const statusFor = id => {
    if (id === rootId) return 'root';
    const item = impactById.get(id);
    if (!item) return 'normal';
    return item.depth === 1 ? 'direct' : 'indirect';
  };

  const elements = [];
  for (const component of graphData.components || []) {
    const impact = impactById.get(component.id);
    elements.push({
      group: 'nodes',
      data: {
        ...component,
        label: component.name,
        status: statusFor(component.id),
        impactDepth: impact?.depth || 0,
        validation: impact?.validation || '',
      },
      classes: statusFor(component.id),
    });
  }

  (graphData.dependencies || []).forEach((dependency, index) => {
    const onImpactPath = impactedIds.has(dependency.source) && impactedIds.has(dependency.target);
    elements.push({
      group: 'edges',
      data: {
        id: `e-${index}-${dependency.source}-${dependency.target}`,
        source: dependency.source,
        target: dependency.target,
        label: dependency.kind,
        kind: dependency.kind,
        documented: dependency.documented,
        onImpactPath,
      },
      classes: `${dependency.documented ? 'documented' : 'hidden'} ${onImpactPath ? 'impact-edge' : ''}`,
    });
  });

  const renderFallback = () => {
    const impacted = impactData?.impacts || [];
    const rows = impacted.length
      ? impacted.map(item => `<li><strong>${item.component}</strong><span>L${item.depth}</span><small>${item.path.join(' → ')}</small></li>`).join('')
      : '<li><strong>Ecosistema cargado</strong><small>La librería visual no está disponible. Ejecuta con acceso al CDN para el grafo interactivo.</small></li>';
    container.innerHTML = `<div class="graph-fallback"><h3>Mapa de impacto</h3><ul>${rows}</ul></div>`;
  };

  if (typeof window.cytoscape !== 'function') {
    renderFallback();
    return;
  }

  const cy = window.cytoscape({
    container,
    elements,
    wheelSensitivity: 0.18,
    minZoom: 0.35,
    maxZoom: 2.2,
    style: [
      {
        selector: 'node',
        style: {
          'background-color': '#163b54',
          'border-color': '#547086',
          'border-width': 2,
          'label': 'data(label)',
          'color': '#eff8ff',
          'font-size': 11,
          'font-weight': 650,
          'text-wrap': 'wrap',
          'text-max-width': 105,
          'text-valign': 'center',
          'text-halign': 'center',
          'width': 86,
          'height': 86,
          'overlay-opacity': 0,
        },
      },
      {
        selector: 'node.root',
        style: {
          'background-color': '#ff5f6d',
          'border-color': '#ffd1d5',
          'border-width': 4,
          'width': 108,
          'height': 108,
          'font-size': 12,
          'shadow-blur': 28,
          'shadow-color': '#ff5f6d',
          'shadow-opacity': 0.55,
        },
      },
      {
        selector: 'node.direct',
        style: {
          'background-color': '#ffc857',
          'border-color': '#fff0b4',
          'color': '#09151f',
          'border-width': 3,
        },
      },
      {
        selector: 'node.indirect',
        style: {
          'background-color': '#43d3ff',
          'border-color': '#bfeeff',
          'color': '#07131f',
          'border-width': 3,
        },
      },
      {
        selector: 'edge',
        style: {
          'width': 1.5,
          'line-color': '#456277',
          'target-arrow-color': '#456277',
          'target-arrow-shape': 'triangle',
          'curve-style': 'bezier',
          'label': 'data(label)',
          'font-size': 8,
          'color': '#86a5ba',
          'text-background-color': '#07131f',
          'text-background-opacity': 0.8,
          'text-background-padding': 2,
          'text-rotation': 'autorotate',
          'overlay-opacity': 0,
        },
      },
      {
        selector: 'edge.impact-edge',
        style: {
          'width': 3,
          'line-color': '#43d3ff',
          'target-arrow-color': '#43d3ff',
          'color': '#c5f4ff',
          'z-index': 10,
        },
      },
      {
        selector: 'edge.hidden',
        style: {
          'line-style': 'dashed',
          'line-color': '#ff6b7a',
          'target-arrow-color': '#ff6b7a',
          'width': 3,
          'color': '#ffb6bd',
        },
      },
      {
        selector: '.dimmed',
        style: { 'opacity': 0.12 },
      },
      {
        selector: 'node:selected',
        style: {
          'border-color': '#ffffff',
          'border-width': 5,
        },
      },
    ],
    layout: impactData
      ? { name: 'breadthfirst', roots: rootId ? `#${rootId}` : undefined, directed: true, spacingFactor: 1.3, padding: 35 }
      : { name: 'cose', animate: false, padding: 35, nodeRepulsion: 520000, idealEdgeLength: 130 },
  });

  const updateInspector = node => {
    const data = node.data();
    const statusLabels = {
      root: 'Cambio raíz',
      direct: 'Impacto directo',
      indirect: 'Impacto indirecto',
      normal: 'No impactado',
    };
    inspector.innerHTML = `
      <span class="eyebrow">Inspector</span>
      <h3>${data.name}</h3>
      <div class="inspector-badge ${data.status}">${statusLabels[data.status] || data.status}</div>
      <dl>
        <div><dt>Tipo</dt><dd>${data.kind}</dd></div>
        <div><dt>Criticidad</dt><dd>C${data.criticality}</dd></div>
        <div><dt>Owner</dt><dd>${data.owner}</dd></div>
        ${data.impactDepth ? `<div><dt>Nivel</dt><dd>L${data.impactDepth}</dd></div>` : ''}
      </dl>
      ${data.validation ? `<p><strong>Validación:</strong><br>${data.validation}</p>` : ''}
    `;
  };

  cy.on('tap', 'node', event => updateInspector(event.target));

  let impactOnly = false;
  toggleButton?.addEventListener('click', () => {
    impactOnly = !impactOnly;
    cy.elements().removeClass('dimmed');
    if (impactOnly) {
      cy.nodes().filter(node => !impactedIds.has(node.id())).addClass('dimmed');
      cy.edges().filter(edge => !edge.data('onImpactPath')).addClass('dimmed');
      toggleButton.textContent = 'Ver ecosistema';
    } else {
      toggleButton.textContent = 'Solo impacto';
    }
    cy.fit(impactOnly ? cy.elements().not('.dimmed') : cy.elements(), 40);
  });

  fitButton?.addEventListener('click', () => cy.fit(cy.elements(), 40));

  if (rootId && cy.getElementById(rootId).length) {
    cy.getElementById(rootId).select();
    updateInspector(cy.getElementById(rootId));
  }

  cy.ready(() => cy.fit(cy.elements(), 40));
})();
