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
  .flow-diagram {
    display: flex;
    justify-content: space-between;
    align-items: stretch;
    margin-top: 15px;
    gap: 6px;
  }
  .flow-item {
    flex: 1;
    background: var(--primary);
    color: white;
    padding: 12px 6px;
    border-radius: 5px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 75px;
  }
  .flow-item h4 {
    margin: 0 0 4px 0;
    font-size: 0.8em;
    color: var(--secondary);
  }
  .flow-item p {
    margin: 0;
    font-size: 0.7em;
    opacity: 0.9;
    line-height: 1.3;
  }
  .flow-arrow {
    font-size: 1.3em;
    color: var(--secondary);
    font-weight: bold;
    display: flex;
    align-items: center;
  }
---

# {{Section Title: e.g. The Process Flow}}

<div class="flow-diagram">
  <div class="flow-item">
    <h4>{{Step A Title}}</h4>
    <p>{{Description of what happens in step A.}}</p>
  </div>
  <div class="flow-arrow">\279E</div>
  <div class="flow-item">
    <h4>{{Step B Title}}</h4>
    <p>{{Description of what happens in step B.}}</p>
  </div>
  <div class="flow-arrow">\279E</div>
  <div class="flow-item">
    <h4>{{Step C Title}}</h4>
    <p>{{Description of what happens in step C.}}</p>
  </div>
</div>

---

## Flow Diagram — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.flow-diagram {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  margin-top: 15px;
  gap: 6px;
}
.flow-item {
  flex: 1;
  background: var(--primary);
  color: white;
  padding: 12px 6px;
  border-radius: 5px;
  text-align: center;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 75px;
}
.flow-item h4 { margin: 0 0 4px 0; font-size: 0.8em; color: var(--secondary); }
.flow-item p { margin: 0; font-size: 0.7em; opacity: 0.9; line-height: 1.3; }
.flow-arrow { font-size: 1.3em; color: var(--secondary); font-weight: bold; display: flex; align-items: center; }
```

```html
<div class="flow-diagram">
  <div class="flow-item">
    <h4>{{Step A Title}}</h4>
    <p>{{Description of step A.}}</p>
  </div>
  <div class="flow-arrow">➔</div>
  <div class="flow-item">
    <h4>{{Step B Title}}</h4>
    <p>{{Description of step B.}}</p>
  </div>
  <div class="flow-arrow">➔</div>
  <div class="flow-item">
    <h4>{{Step C Title}}</h4>
    <p>{{Description of step C.}}</p>
  </div>
</div>
```
