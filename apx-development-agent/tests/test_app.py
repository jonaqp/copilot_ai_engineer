from app import app
def test_health():
    c=app.test_client(); r=c.get('/health'); assert r.status_code==200; assert r.get_json()['status']=='ok'
def test_plan_requires_task():
    c=app.test_client(); assert c.post('/api/agent-plan',json={}).status_code==400
def test_plan():
    c=app.test_client(); r=c.post('/api/agent-plan',json={'task':'demo'}); assert r.status_code==200; assert r.get_json()['skills']
