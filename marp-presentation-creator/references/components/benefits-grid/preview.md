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
  .benefits-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    margin-top: 15px;
  }
  .benefit-card {
    display: flex;
    align-items: center;
    gap: 15px;
    background: #ffffff;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    border: 1px solid rgba(0,168,204,0.2);
  }
  .benefit-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 50px;
    background: rgba(0,168,204,0.1);
    color: var(--primary);
    font-size: 1.5em;
    border-radius: 50%;
    flex-shrink: 0;
  }
  .benefit-text h4 {
    margin: 0 0 5px 0;
    color: var(--primary);
    font-size: 1em;
  }
  .benefit-text p {
    margin: 0;
    font-size: 0.8em;
    color: #555;
    line-height: 1.3;
  }
---

# {{Section Title: e.g. Key Benefits}}

<div class="benefits-grid">
  <div class="benefit-card">
    <div class="benefit-icon">{{Icon}}</div>
    <div class="benefit-text">
      <h4>{{Benefit One Name}}</h4>
      <p>{{Description of this benefit and why it matters.}}</p>
    </div>
  </div>
  <div class="benefit-card">
    <div class="benefit-icon">{{Icon}}</div>
    <div class="benefit-text">
      <h4>{{Benefit Two Name}}</h4>
      <p>{{Description of this benefit and why it matters.}}</p>
    </div>
  </div>
  <div class="benefit-card">
    <div class="benefit-icon">{{Icon}}</div>
    <div class="benefit-text">
      <h4>{{Benefit Three Name}}</h4>
      <p>{{Description of this benefit and why it matters.}}</p>
    </div>
  </div>
  <div class="benefit-card">
    <div class="benefit-icon">{{Icon}}</div>
    <div class="benefit-text">
      <h4>{{Benefit Four Name}}</h4>
      <p>{{Description of this benefit and why it matters.}}</p>
    </div>
  </div>
</div>

---

## Benefits Grid — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.benefits-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
  margin-top: 15px;
}
.benefit-card {
  display: flex;
  align-items: center;
  gap: 15px;
  background: #ffffff;
  padding: 15px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.06);
  border: 1px solid rgba(0,168,204,0.2);
}
.benefit-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px; height: 50px;
  background: rgba(0,168,204,0.1);
  color: var(--primary);
  font-size: 1.5em;
  border-radius: 50%;
  flex-shrink: 0;
}
.benefit-text h4 { margin: 0 0 5px 0; color: var(--primary); font-size: 1em; }
.benefit-text p { margin: 0; font-size: 0.8em; color: #555; line-height: 1.3; }
```

```html
<div class="benefits-grid">
  <div class="benefit-card">
    <div class="benefit-icon">{{Icon}}</div>
    <div class="benefit-text">
      <h4>{{Benefit One Name}}</h4>
      <p>{{Description of this benefit.}}</p>
    </div>
  </div>
  <div class="benefit-card">
    <div class="benefit-icon">{{Icon}}</div>
    <div class="benefit-text">
      <h4>{{Benefit Two Name}}</h4>
      <p>{{Description of this benefit.}}</p>
    </div>
  </div>
  <div class="benefit-card">
    <div class="benefit-icon">{{Icon}}</div>
    <div class="benefit-text">
      <h4>{{Benefit Three Name}}</h4>
      <p>{{Description of this benefit.}}</p>
    </div>
  </div>
  <div class="benefit-card">
    <div class="benefit-icon">{{Icon}}</div>
    <div class="benefit-text">
      <h4>{{Benefit Four Name}}</h4>
      <p>{{Description of this benefit.}}</p>
    </div>
  </div>
</div>
```
