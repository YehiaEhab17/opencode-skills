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
  .layered-blocks {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 15px;
    align-items: center;
    width: 100%;
    box-sizing: border-box;
  }
  .layer {
    background: #ffffff;
    padding: 14px 24px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    width: 92%;
    border-left: 8px solid var(--secondary);
    display: flex;
    align-items: center;
    gap: 20px;
    box-sizing: border-box;
  }
  .layer:nth-child(2) { border-left-color: var(--primary); }
  .layer:nth-child(3) { border-left-color: #2ECC71; }
  .layer:nth-child(4) { border-left-color: #F39C12; }
  .layer h4 {
    margin: 0;
    color: var(--primary);
    width: 200px;
    flex-shrink: 0;
    font-size: 0.95em;
  }
  .layer p {
    margin: 0;
    font-size: 0.85em;
    color: #555;
  }
---

# {{Section Title: e.g. Architecture Overview}}

<div class="layered-blocks">
  <div class="layer">
    <h4>{{Layer One Name}}</h4>
    <p>{{Description of this layer or topic. Explain what it covers.}}</p>
  </div>
  <div class="layer">
    <h4>{{Layer Two Name}}</h4>
    <p>{{Description of this layer or topic. Explain what it covers.}}</p>
  </div>
  <div class="layer">
    <h4>{{Layer Three Name}}</h4>
    <p>{{Description of this layer or topic. Explain what it covers.}}</p>
  </div>
</div>

---

## Layered Blocks — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.layered-blocks {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 15px;
  align-items: center;
  width: 100%;
  box-sizing: border-box;
}
.layer {
  background: #ffffff;
  padding: 14px 24px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.08);
  width: 92%;
  border-left: 8px solid var(--secondary);
  display: flex;
  align-items: center;
  gap: 20px;
  box-sizing: border-box;
}
.layer:nth-child(2) { border-left-color: var(--primary); }
.layer:nth-child(3) { border-left-color: #2ECC71; }
.layer:nth-child(4) { border-left-color: #F39C12; }
.layer h4 { margin: 0; color: var(--primary); width: 200px; flex-shrink: 0; font-size: 0.95em; }
.layer p { margin: 0; font-size: 0.85em; color: #555; }
```

```html
<div class="layered-blocks">
  <div class="layer">
    <h4>{{Layer One Name}}</h4>
    <p>{{Description of this layer.}}</p>
  </div>
  <div class="layer">
    <h4>{{Layer Two Name}}</h4>
    <p>{{Description of this layer.}}</p>
  </div>
  <div class="layer">
    <h4>{{Layer Three Name}}</h4>
    <p>{{Description of this layer.}}</p>
  </div>
</div>
```
