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
  .stripe-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 15px;
  }
  .stripe {
    display: flex;
    align-items: center;
    background: #ffffff;
    padding: 10px 20px;
    border-radius: 8px;
    box-shadow: 0 3px 8px rgba(0,0,0,0.05);
  }
  .stripe-title {
    width: 220px;
    font-weight: bold;
    color: var(--primary);
    font-size: 0.95em;
    flex-shrink: 0;
    border-right: 2px solid rgba(0,168,204,0.3);
    padding-right: 15px;
    margin-right: 15px;
  }
  .stripe p {
    margin: 0;
    font-size: 0.85em;
    color: #555;
  }
---

# {{Section Title: e.g. Market Analysis}}

<div class="stripe-list">
  <div class="stripe">
    <div class="stripe-title">{{Label One}}</div>
    <p>{{Description of this item. What it means, why it matters.}}</p>
  </div>
  <div class="stripe">
    <div class="stripe-title">{{Label Two}}</div>
    <p>{{Description of this item. What it means, why it matters.}}</p>
  </div>
  <div class="stripe">
    <div class="stripe-title">{{Label Three}}</div>
    <p>{{Description of this item. What it means, why it matters.}}</p>
  </div>
  <div class="stripe">
    <div class="stripe-title">{{Label Four}}</div>
    <p>{{Description of this item. What it means, why it matters.}}</p>
  </div>
</div>

---

## Horizontal Stripes — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.stripe-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 15px;
}
.stripe {
  display: flex;
  align-items: center;
  background: #ffffff;
  padding: 10px 20px;
  border-radius: 8px;
  box-shadow: 0 3px 8px rgba(0,0,0,0.05);
}
.stripe-title {
  width: 220px;
  font-weight: bold;
  color: var(--primary);
  font-size: 0.95em;
  flex-shrink: 0;
  border-right: 2px solid rgba(0,168,204,0.3);
  padding-right: 15px;
  margin-right: 15px;
}
.stripe p { margin: 0; font-size: 0.85em; color: #555; }
```

```html
<div class="stripe-list">
  <div class="stripe">
    <div class="stripe-title">{{Label One}}</div>
    <p>{{Description of this item.}}</p>
  </div>
  <div class="stripe">
    <div class="stripe-title">{{Label Two}}</div>
    <p>{{Description of this item.}}</p>
  </div>
  <div class="stripe">
    <div class="stripe-title">{{Label Three}}</div>
    <p>{{Description of this item.}}</p>
  </div>
  <div class="stripe">
    <div class="stripe-title">{{Label Four}}</div>
    <p>{{Description of this item.}}</p>
  </div>
</div>
```
