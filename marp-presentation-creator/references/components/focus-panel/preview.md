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
  .focus-panel {
    display: flex;
    gap: 20px;
    margin-top: 20px;
    align-items: stretch;
  }
  .fp-main {
    flex: 1.2;
    background: linear-gradient(135deg, var(--primary) 0%, #001f3f 100%);
    color: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .fp-main h3 {
    color: var(--secondary);
    border: none;
    margin: 0 0 10px 0;
    font-size: 1.3em;
  }
  .fp-main p {
    font-size: 0.9em;
    line-height: 1.5;
    margin: 0;
    opacity: 0.9;
  }
  .fp-list {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: space-between;
  }
  .fp-item {
    background: #ffffff;
    padding: 12px 15px;
    border-left: 4px solid var(--secondary);
    box-shadow: 0 4px 10px rgba(0,0,0,0.04);
  }
  .fp-item h4 {
    margin: 0 0 3px 0;
    color: var(--primary);
    font-size: 0.95em;
  }
  .fp-item p {
    margin: 0;
    font-size: 0.8em;
    color: #555;
    line-height: 1.3;
  }
---

# {{Section Title}}

<div class="focus-panel">
  <div class="fp-main">
    <h3>{{Main Statement or Thesis}}</h3>
    <p>{{The core message that everything supports. A single, powerful sentence.}}</p>
  </div>
  <div class="fp-list">
    <div class="fp-item">
      <h4>{{Supporting Point One}}</h4>
      <p>{{Detail explaining this point.}}</p>
    </div>
    <div class="fp-item">
      <h4>{{Supporting Point Two}}</h4>
      <p>{{Detail explaining this point.}}</p>
    </div>
    <div class="fp-item">
      <h4>{{Supporting Point Three}}</h4>
      <p>{{Detail explaining this point.}}</p>
    </div>
  </div>
</div>

---

## Focus Panel — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.focus-panel {
  display: flex;
  gap: 20px;
  margin-top: 20px;
  align-items: stretch;
}
.fp-main {
  flex: 1.2;
  background: linear-gradient(135deg, var(--primary) 0%, #001f3f 100%);
  color: white;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.15);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.fp-main h3 { color: var(--secondary); border: none; margin: 0 0 10px 0; font-size: 1.3em; }
.fp-main p { font-size: 0.9em; line-height: 1.5; margin: 0; opacity: 0.9; }
.fp-list { flex: 1; display: flex; flex-direction: column; gap: 10px; justify-content: space-between; }
.fp-item {
  background: #ffffff;
  padding: 12px 15px;
  border-left: 4px solid var(--secondary);
  box-shadow: 0 4px 10px rgba(0,0,0,0.04);
}
.fp-item h4 { margin: 0 0 3px 0; color: var(--primary); font-size: 0.95em; }
.fp-item p { margin: 0; font-size: 0.8em; color: #555; line-height: 1.3; }
```

```html
<div class="focus-panel">
  <div class="fp-main">
    <h3>{{Main Statement}}</h3>
    <p>{{The core message.}}</p>
  </div>
  <div class="fp-list">
    <div class="fp-item">
      <h4>{{Supporting Point One}}</h4>
      <p>{{Detail explaining this point.}}</p>
    </div>
    <div class="fp-item">
      <h4>{{Supporting Point Two}}</h4>
      <p>{{Detail explaining this point.}}</p>
    </div>
    <div class="fp-item">
      <h4>{{Supporting Point Three}}</h4>
      <p>{{Detail explaining this point.}}</p>
    </div>
  </div>
</div>
```
