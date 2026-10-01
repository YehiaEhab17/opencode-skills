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
  .split-card-container {
    display: flex;
    background: #ffffff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    margin-top: 20px;
  }
  .split-half {
    flex: 1;
    padding: 25px;
  }
  .split-half:first-child {
    border-right: 2px dashed rgba(0,168,204,0.3);
  }
  .split-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }
  .split-header h3 {
    margin: 0;
    font-size: 1.2em;
    color: var(--primary);
  }
  .s-icon {
    font-size: 1.5em;
  }
  .split-half p {
    margin: 0;
    font-size: 0.9em;
    color: #555;
    line-height: 1.5;
  }
---

# {{Slide Title: e.g. Comparison}}

<div class="split-card-container">
  <div class="split-half">
    <div class="split-header">
      <div class="s-icon">{{Icon}}</div>
      <h3>{{Option A Name}}</h3>
    </div>
    <p>{{Description of Option A with its benefits and features. Keep it balanced.}}</p>
  </div>
  <div class="split-half">
    <div class="split-header">
      <div class="s-icon">{{Icon}}</div>
      <h3>{{Option B Name}}</h3>
    </div>
    <p>{{Description of Option B with its benefits and features. Keep it balanced.}}</p>
  </div>
</div>

---

## Split Card — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.split-card-container {
  display: flex;
  background: #ffffff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 20px rgba(0,0,0,0.08);
  margin-top: 20px;
}
.split-half { flex: 1; padding: 25px; }
.split-half:first-child { border-right: 2px dashed rgba(0,168,204,0.3); }
.split-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.split-header h3 { margin: 0; font-size: 1.2em; color: var(--primary); }
.s-icon { font-size: 1.5em; }
.split-half p { margin: 0; font-size: 0.9em; color: #555; line-height: 1.5; }
```

```html
<div class="split-card-container">
  <div class="split-half">
    <div class="split-header">
      <div class="s-icon">{{Icon}}</div>
      <h3>{{Option A Name}}</h3>
    </div>
    <p>{{Description of Option A.}}</p>
  </div>
  <div class="split-half">
    <div class="split-header">
      <div class="s-icon">{{Icon}}</div>
      <h3>{{Option B Name}}</h3>
    </div>
    <p>{{Description of Option B.}}</p>
  </div>
</div>
```
