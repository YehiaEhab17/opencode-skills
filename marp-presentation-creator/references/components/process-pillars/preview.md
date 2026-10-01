---
marp: true
theme: default
size: 16:9
style: |
  :root {
    --primary: #003366;
    --secondary: #00A8CC;
  }
  section {
    font-family: 'Segoe UI', system-ui, sans-serif;
    background-color: #F4F7F6;
    color: #2C3E50;
    padding: 50px 60px;
  }
  h1 {
    color: var(--primary);
    font-size: 2em;
    margin-bottom: 0.5em;
  }
  h1::after {
    content: '';
    display: block;
    width: 60px;
    height: 5px;
    background-color: var(--secondary);
    margin-top: 8px;
    border-radius: 3px;
  }

  /* Component CSS */
  .pillars {
    display: flex;
    justify-content: space-between;
    align-items: stretch;
    gap: 15px;
    margin-top: 10px;
  }
  .pillar {
    flex: 1;
    background: linear-gradient(180deg, #ffffff 0%, #f9fbfd 100%);
    border-top: 6px solid var(--primary);
    border-radius: 10px;
    padding: 15px 15px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .pillar-icon {
    font-size: 1.8em;
    margin-bottom: 5px;
  }
  .pillar h4 {
    color: var(--primary);
    font-size: 1.1em;
    margin: 0 0 10px 0;
  }
  .pillar p {
    font-size: 0.85em;
    color: #555;
    line-height: 1.5;
    margin: 0;
  }
---

# {{Section Title: e.g. Core Principles}}

<div class="pillars">
  <div class="pillar">
    <div class="pillar-icon">{{Icon}}</div>
    <h4>{{Principle One Name}}</h4>
    <p>{{Description of this principle or value. Keep it concise.}}</p>
  </div>
  <div class="pillar">
    <div class="pillar-icon">{{Icon}}</div>
    <h4>{{Principle Two Name}}</h4>
    <p>{{Description of this principle or value. Keep it concise.}}</p>
  </div>
  <div class="pillar">
    <div class="pillar-icon">{{Icon}}</div>
    <h4>{{Principle Three Name}}</h4>
    <p>{{Description of this principle or value. Keep it concise.}}</p>
  </div>
</div>

---

## Process Pillars — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.pillars {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  gap: 15px;
  margin-top: 10px;
}
.pillar {
  flex: 1;
  background: linear-gradient(180deg, #ffffff 0%, #f9fbfd 100%);
  border-top: 6px solid var(--primary);
  border-radius: 10px;
  padding: 15px 15px;
  text-align: center;
  box-shadow: 0 5px 15px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.pillar-icon { font-size: 1.8em; margin-bottom: 5px; }
.pillar h4 { color: var(--primary); font-size: 1.1em; margin: 0 0 10px 0; }
.pillar p { font-size: 0.85em; color: #555; line-height: 1.5; margin: 0; }
```

```html
<div class="pillars">
  <div class="pillar">
    <div class="pillar-icon">{{Icon}}</div>
    <h4>{{Principle One Name}}</h4>
    <p>{{Description of this principle.}}</p>
  </div>
  <div class="pillar">
    <div class="pillar-icon">{{Icon}}</div>
    <h4>{{Principle Two Name}}</h4>
    <p>{{Description of this principle.}}</p>
  </div>
  <div class="pillar">
    <div class="pillar-icon">{{Icon}}</div>
    <h4>{{Principle Three Name}}</h4>
    <p>{{Description of this principle.}}</p>
  </div>
</div>
```
