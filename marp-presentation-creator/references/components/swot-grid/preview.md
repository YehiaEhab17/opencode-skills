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
    display: none;
  }

  /* Component CSS */
  .swot-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 15px;
    margin-top: 10px;
  }
  .swot-item {
    padding: 15px 20px;
    border-radius: 10px;
    color: white;
    position: relative;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
  }
  .swot-item h2 {
    margin: 0 0 10px 0;
    font-size: 1.3em;
    color: white;
    position: relative;
    z-index: 2;
  }
  .swot-item ul {
    position: relative;
    z-index: 2;
    font-size: 0.85em;
    margin: 0;
    padding-left: 15px;
    line-height: 1.4;
  }
  .swot-item li { margin-bottom: 5px; }
  .swot-bg {
    position: absolute;
    top: -5px;
    right: 10px;
    font-size: 5em;
    opacity: 0.15;
    font-weight: 800;
    line-height: 1;
    z-index: 1;
    font-family: Impact, sans-serif;
  }
  .s-box { background: linear-gradient(135deg, #27AE60, #2ECC71); }
  .w-box { background: linear-gradient(135deg, #E67E22, #F39C12); }
  .o-box { background: linear-gradient(135deg, #2980B9, #3498DB); }
  .t-box { background: linear-gradient(135deg, #C0392B, #E74C3C); }
---

# {{Analysis Title: e.g. Competitive Analysis}}

<div class="swot-grid">
  <div class="swot-item s-box">
    <div class="swot-bg">S</div>
    <h2>Strengths</h2>
    <ul>
      <li>{{Strength point one}}</li>
      <li>{{Strength point two}}</li>
    </ul>
  </div>
  <div class="swot-item w-box">
    <div class="swot-bg">W</div>
    <h2>Weaknesses</h2>
    <ul>
      <li>{{Weakness point one}}</li>
      <li>{{Weakness point two}}</li>
    </ul>
  </div>
  <div class="swot-item o-box">
    <div class="swot-bg">O</div>
    <h2>Opportunities</h2>
    <ul>
      <li>{{Opportunity point one}}</li>
      <li>{{Opportunity point two}}</li>
    </ul>
  </div>
  <div class="swot-item t-box">
    <div class="swot-bg">T</div>
    <h2>Threats</h2>
    <ul>
      <li>{{Threat point one}}</li>
      <li>{{Threat point two}}</li>
    </ul>
  </div>
</div>

---

## SWOT Grid — Template

```css
.swot-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 15px;
  margin-top: 10px;
}
.swot-item {
  padding: 15px 20px;
  border-radius: 10px;
  color: white;
  position: relative;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
}
.swot-item h2 { margin: 0 0 10px 0; font-size: 1.3em; color: white; position: relative; z-index: 2; }
.swot-item ul { position: relative; z-index: 2; font-size: 0.85em; margin: 0; padding-left: 15px; line-height: 1.4; }
.swot-item li { margin-bottom: 5px; }
.swot-bg {
  position: absolute;
  top: -5px; right: 10px;
  font-size: 5em;
  opacity: 0.15;
  font-weight: 800;
  z-index: 1;
  font-family: Impact, sans-serif;
}
.s-box { background: linear-gradient(135deg, #27AE60, #2ECC71); }
.w-box { background: linear-gradient(135deg, #E67E22, #F39C12); }
.o-box { background: linear-gradient(135deg, #2980B9, #3498DB); }
.t-box { background: linear-gradient(135deg, #C0392B, #E74C3C); }
```

```html
<div class="swot-grid">
  <div class="swot-item s-box">
    <div class="swot-bg">S</div>
    <h2>Strengths</h2>
    <ul>
      <li>{{Strength point one}}</li>
      <li>{{Strength point two}}</li>
    </ul>
  </div>
  <div class="swot-item w-box">
    <div class="swot-bg">W</div>
    <h2>Weaknesses</h2>
    <ul>
      <li>{{Weakness point one}}</li>
      <li>{{Weakness point two}}</li>
    </ul>
  </div>
  <div class="swot-item o-box">
    <div class="swot-bg">O</div>
    <h2>Opportunities</h2>
    <ul>
      <li>{{Opportunity point one}}</li>
      <li>{{Opportunity point two}}</li>
    </ul>
  </div>
  <div class="swot-item t-box">
    <div class="swot-bg">T</div>
    <h2>Threats</h2>
    <ul>
      <li>{{Threat point one}}</li>
      <li>{{Threat point two}}</li>
    </ul>
  </div>
</div>
```
