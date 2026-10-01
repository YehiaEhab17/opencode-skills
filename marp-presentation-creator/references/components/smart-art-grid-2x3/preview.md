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
  .smart-art-grid-2x3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 10px;
  }
  .smart-art-card {
    background: #ffffff;
    border: 2px solid #e2e8f0;
    border-top: 5px solid var(--secondary);
    border-radius: 8px;
    padding: 12px 14px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .smart-art-card img {
    width: 36px;
    height: 36px;
    margin-bottom: 8px;
  }
  .smart-art-card h3 {
    font-size: 0.95em;
    margin: 0 0 8px 0;
    color: var(--primary);
  }
  .smart-art-card p {
    font-size: 0.78em;
    color: #555;
    margin: 0;
    line-height: 1.3;
  }
---

# {{Section Title: e.g. Key Features}}

<div class="smart-art-grid-2x3">
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item One Title}}</h3>
    <p>{{Brief description of this item. Keep it concise.}}</p>
  </div>
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item Two Title}}</h3>
    <p>{{Brief description of this item. Keep it concise.}}</p>
  </div>
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item Three Title}}</h3>
    <p>{{Brief description of this item. Keep it concise.}}</p>
  </div>
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item Four Title}}</h3>
    <p>{{Brief description of this item. Keep it concise.}}</p>
  </div>
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item Five Title}}</h3>
    <p>{{Brief description of this item. Keep it concise.}}</p>
  </div>
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item Six Title}}</h3>
    <p>{{Brief description of this item. Keep it concise.}}</p>
  </div>
</div>

---

## Smart Art Grid 2x3 — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.smart-art-grid-2x3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-top: 10px;
}
.smart-art-card {
  background: #ffffff;
  border: 2px solid #e2e8f0;
  border-top: 5px solid var(--secondary);
  border-radius: 8px;
  padding: 12px 14px;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
  align-items: center;
}
.smart-art-card img { width: 36px; height: 36px; margin-bottom: 8px; }
.smart-art-card h3 { font-size: 0.95em; margin: 0 0 8px 0; color: var(--primary); }
.smart-art-card p { font-size: 0.78em; color: #555; margin: 0; line-height: 1.3; }
```

```html
<div class="smart-art-grid-2x3">
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item One Title}}</h3>
    <p>{{Brief description.}}</p>
  </div>
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item Two Title}}</h3>
    <p>{{Brief description.}}</p>
  </div>
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item Three Title}}</h3>
    <p>{{Brief description.}}</p>
  </div>
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item Four Title}}</h3>
    <p>{{Brief description.}}</p>
  </div>
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item Five Title}}</h3>
    <p>{{Brief description.}}</p>
  </div>
  <div class="smart-art-card">
    <img src="{{icon-url}}" alt="{{Icon}}" />
    <h3>{{Item Six Title}}</h3>
    <p>{{Brief description.}}</p>
  </div>
</div>
```
