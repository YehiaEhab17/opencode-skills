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
  .stat-container {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-top: 15px;
    max-width: 500px;
    margin-left: auto;
    margin-right: auto;
  }
  .stat-box {
    background: var(--primary);
    color: white;
    padding: 15px;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.15);
    flex: 1;
    margin-bottom: 0;
  }
  .stat-num {
    font-size: 2em;
    font-weight: bold;
    color: var(--secondary);
    margin-bottom: 5px;
  }
  .stat-desc {
    font-size: 0.85em;
    opacity: 0.9;
  }
---

# {{Section Title: e.g. Financial Overview}}

<div class="stat-container">
  <div class="stat-box">
    <div class="stat-num">{{Key Figure}}</div>
    <div class="stat-desc">{{Description of what this figure represents.}}</div>
  </div>
  <div class="stat-box" style="background: var(--secondary);">
    <div class="stat-num">{{Key Figure}}</div>
    <div class="stat-desc">{{Description of what this figure represents.}}</div>
  </div>
</div>

---

## Stat Boxes — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.stat-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 15px;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}
.stat-box {
  background: var(--primary);
  color: white;
  padding: 15px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 5px 15px rgba(0,0,0,0.15);
}
.stat-num { font-size: 2em; font-weight: bold; color: var(--secondary); margin-bottom: 5px; }
.stat-desc { font-size: 0.85em; opacity: 0.9; }
```

```html
<div class="stat-container">
  <div class="stat-box">
    <div class="stat-num">{{Key Figure}}</div>
    <div class="stat-desc">{{Description of this figure.}}</div>
  </div>
  <div class="stat-box" style="background: var(--secondary);">
    <div class="stat-num">{{Key Figure}}</div>
    <div class="stat-desc">{{Description of this figure.}}</div>
  </div>
</div>
```
