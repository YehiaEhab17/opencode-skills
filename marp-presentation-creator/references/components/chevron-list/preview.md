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
  .chevron-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 10px;
  }
  .chevron-item {
    background: #ffffff;
    padding: 10px 15px 10px 40px;
    border-radius: 8px;
    position: relative;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    border-left: 5px solid var(--secondary);
    margin-left: 10px;
  }
  .chevron-item::before {
    content: '\279E';
    position: absolute;
    left: 10px;
    top: 12px;
    color: var(--secondary);
    font-size: 1.1em;
  }
  .chevron-item h4 {
    margin: 0 0 5px 0;
    color: var(--primary);
    font-size: 1.05em;
  }
  .chevron-item p {
    margin: 0;
    font-size: 0.85em;
    color: #555;
    line-height: 1.4;
  }
---

# {{Section Title: e.g. The Problem}}

<div class="chevron-list">
  <div class="chevron-item">
    <h4>{{Issue One Name}}</h4>
    <p>{{Description of this issue. Keep it specific and actionable.}}</p>
  </div>
  <div class="chevron-item">
    <h4>{{Issue Two Name}}</h4>
    <p>{{Description of this issue. Keep it specific and actionable.}}</p>
  </div>
  <div class="chevron-item">
    <h4>{{Issue Three Name}}</h4>
    <p>{{Description of this issue. Keep it specific and actionable.}}</p>
  </div>
</div>

---

## Chevron List — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.chevron-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 10px;
}
.chevron-item {
  background: #ffffff;
  padding: 10px 15px 10px 40px;
  border-radius: 8px;
  position: relative;
  box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  border-left: 5px solid var(--secondary);
  margin-left: 10px;
}
.chevron-item::before {
  content: '\279E';
  position: absolute;
  left: 10px;
  top: 12px;
  color: var(--secondary);
  font-size: 1.1em;
}
.chevron-item h4 { margin: 0 0 5px 0; color: var(--primary); font-size: 1.05em; }
.chevron-item p { margin: 0; font-size: 0.85em; color: #555; line-height: 1.4; }
```

```html
<div class="chevron-list">
  <div class="chevron-item">
    <h4>{{Issue One Name}}</h4>
    <p>{{Description of this issue.}}</p>
  </div>
  <div class="chevron-item">
    <h4>{{Issue Two Name}}</h4>
    <p>{{Description of this issue.}}</p>
  </div>
  <div class="chevron-item">
    <h4>{{Issue Three Name}}</h4>
    <p>{{Description of this issue.}}</p>
  </div>
</div>
```
