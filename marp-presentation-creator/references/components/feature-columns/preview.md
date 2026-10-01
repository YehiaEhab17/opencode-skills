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
  .feature-cols {
    display: flex;
    gap: 15px;
    margin-top: 20px;
  }
  .f-col {
    flex: 1;
    background: #ffffff;
    padding: 15px 10px;
    border-radius: 8px;
    text-align: center;
    border: 1px solid rgba(0,51,102,0.1);
    box-shadow: 0 4px 10px rgba(0,0,0,0.03);
  }
  .f-icon {
    width: 40px;
    height: 40px;
    background: var(--secondary);
    color: white;
    border-radius: 50%;
    line-height: 40px;
    font-size: 1.2em;
    margin: 0 auto 10px auto;
  }
  .f-col h4 {
    margin: 0 0 5px 0;
    color: var(--primary);
    font-size: 0.95em;
  }
  .f-col p {
    margin: 0;
    font-size: 0.75em;
    color: #555;
    line-height: 1.4;
  }
---

# {{Section Title: e.g. Platform Features}}

<div class="feature-cols">
  <div class="f-col">
    <div class="f-icon">{{Icon}}</div>
    <h4>{{Feature One Name}}</h4>
    <p>{{Brief description of this feature.}}</p>
  </div>
  <div class="f-col">
    <div class="f-icon">{{Icon}}</div>
    <h4>{{Feature Two Name}}</h4>
    <p>{{Brief description of this feature.}}</p>
  </div>
  <div class="f-col">
    <div class="f-icon">{{Icon}}</div>
    <h4>{{Feature Three Name}}</h4>
    <p>{{Brief description of this feature.}}</p>
  </div>
  <div class="f-col">
    <div class="f-icon">{{Icon}}</div>
    <h4>{{Feature Four Name}}</h4>
    <p>{{Brief description of this feature.}}</p>
  </div>
</div>

---

## Feature Columns — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.feature-cols {
  display: flex;
  gap: 15px;
  margin-top: 20px;
}
.f-col {
  flex: 1;
  background: #ffffff;
  padding: 15px 10px;
  border-radius: 8px;
  text-align: center;
  border: 1px solid rgba(0,51,102,0.1);
  box-shadow: 0 4px 10px rgba(0,0,0,0.03);
}
.f-icon {
  width: 40px; height: 40px;
  background: var(--secondary);
  color: white;
  border-radius: 50%;
  line-height: 40px;
  font-size: 1.2em;
  margin: 0 auto 10px auto;
}
.f-col h4 { margin: 0 0 5px 0; color: var(--primary); font-size: 0.95em; }
.f-col p { margin: 0; font-size: 0.75em; color: #555; line-height: 1.4; }
```

```html
<div class="feature-cols">
  <div class="f-col">
    <div class="f-icon">{{Icon}}</div>
    <h4>{{Feature One Name}}</h4>
    <p>{{Brief description.}}</p>
  </div>
  <div class="f-col">
    <div class="f-icon">{{Icon}}</div>
    <h4>{{Feature Two Name}}</h4>
    <p>{{Brief description.}}</p>
  </div>
  <div class="f-col">
    <div class="f-icon">{{Icon}}</div>
    <h4>{{Feature Three Name}}</h4>
    <p>{{Brief description.}}</p>
  </div>
  <div class="f-col">
    <div class="f-icon">{{Icon}}</div>
    <h4>{{Feature Four Name}}</h4>
    <p>{{Brief description.}}</p>
  </div>
</div>
```
