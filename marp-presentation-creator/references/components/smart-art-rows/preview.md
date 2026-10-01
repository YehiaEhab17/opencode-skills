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
  .smart-art-rows {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 10px;
  }
  .smart-art-row-item {
    display: flex;
    align-items: center;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 5px solid var(--secondary);
    border-radius: 8px;
    padding: 10px 15px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }
  .smart-art-row-item.danger {
    border-left-color: #e53e3e;
  }
  .smart-art-row-item.success {
    border-left-color: #38a169;
  }
  .smart-art-row-item img {
    width: 36px;
    height: 36px;
    margin-right: 15px;
    flex-shrink: 0;
  }
  .smart-art-row-item h3 {
    margin: 0 0 3px 0;
    font-size: 1.05em;
    color: var(--primary);
  }
  .smart-art-row-item p {
    margin: 0;
    font-size: 0.85em;
    color: #555;
    line-height: 1.3;
  }
---

# {{Section Title: e.g. Key Tips}}

<div class="smart-art-rows">
  <div class="smart-art-row-item">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <div>
      <h3>{{Tip One Title}}</h3>
      <p>{{Brief description of the tip or action item.}}</p>
    </div>
  </div>
  <div class="smart-art-row-item danger">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <div>
      <h3>{{Warning Title}}</h3>
      <p>{{Brief description of the warning or "what to avoid".}}</p>
    </div>
  </div>
  <div class="smart-art-row-item success">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <div>
      <h3>{{Positive Action Title}}</h3>
      <p>{{Brief description of the positive action or best practice.}}</p>
    </div>
  </div>
</div>

---

## Smart Art Rows — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.smart-art-rows {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 10px;
}
.smart-art-row-item {
  display: flex;
  align-items: center;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-left: 5px solid var(--secondary);
  border-radius: 8px;
  padding: 10px 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.smart-art-row-item.danger { border-left-color: #e53e3e; }
.smart-art-row-item.success { border-left-color: #38a169; }
.smart-art-row-item img { width: 36px; height: 36px; margin-right: 15px; flex-shrink: 0; }
.smart-art-row-item h3 { margin: 0 0 3px 0; font-size: 1.05em; color: var(--primary); }
.smart-art-row-item p { margin: 0; font-size: 0.85em; color: #555; line-height: 1.3; }
```

```html
<div class="smart-art-rows">
  <div class="smart-art-row-item">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <div>
      <h3>{{Tip Title}}</h3>
      <p>{{Description of the tip.}}</p>
    </div>
  </div>
  <div class="smart-art-row-item danger">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <div>
      <h3>{{Warning Title}}</h3>
    <p>{{Description of the warning.}}</p>
    </div>
  </div>
  <div class="smart-art-row-item success">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <div>
      <h3>{{Positive Action Title}}</h3>
      <p>{{Description of the positive action.}}</p>
    </div>
  </div>
</div>
```
