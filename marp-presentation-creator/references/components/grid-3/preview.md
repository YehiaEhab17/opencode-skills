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
  .grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 30px;
  }
  .card {
    background: #ffffff;
    padding: 15px 20px;
    border-radius: 10px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    border-left: 4px solid var(--secondary);
  }
  .card-icon {
    font-size: 2em;
    margin-bottom: 5px;
  }
  .card h3 {
    margin: 0 0 5px 0;
    color: var(--primary);
    font-size: 1.1em;
  }
  .card p {
    margin: 0;
    font-size: 0.9em;
    color: #555;
    line-height: 1.5;
  }
---

# {{Section Title}}

<div class="grid-3">
  <div class="card" style="text-align: center;">
    <div class="card-icon">{{Icon}}</div>
    <h3>{{Pillar One Name}}</h3>
    <p>{{Description of this pillar or item. Keep concise.}}</p>
  </div>
  <div class="card" style="text-align: center;">
    <div class="card-icon">{{Icon}}</div>
    <h3>{{Pillar Two Name}}</h3>
    <p>{{Description of this pillar or item. Keep concise.}}</p>
  </div>
  <div class="card" style="text-align: center;">
    <div class="card-icon">{{Icon}}</div>
    <h3>{{Pillar Three Name}}</h3>
    <p>{{Description of this pillar or item. Keep concise.}}</p>
  </div>
</div>

---

## Grid 3 — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 30px;
}
.card {
  background: #ffffff;
  padding: 15px 20px;
  border-radius: 10px;
  box-shadow: 0 6px 15px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
  border-left: 4px solid var(--secondary);
}
.card-icon { font-size: 2em; margin-bottom: 5px; }
.card h3 { margin: 0 0 5px 0; color: var(--primary); font-size: 1.1em; }
.card p { margin: 0; font-size: 0.9em; color: #555; line-height: 1.5; }
```

```html
<div class="grid-3">
  <div class="card" style="text-align: center;">
    <div class="card-icon">{{Icon}}</div>
    <h3>{{Pillar One Name}}</h3>
    <p>{{Description.}}</p>
  </div>
  <div class="card" style="text-align: center;">
    <div class="card-icon">{{Icon}}</div>
    <h3>{{Pillar Two Name}}</h3>
    <p>{{Description.}}</p>
  </div>
  <div class="card" style="text-align: center;">
    <div class="card-icon">{{Icon}}</div>
    <h3>{{Pillar Three Name}}</h3>
    <p>{{Description.}}</p>
  </div>
</div>
```
