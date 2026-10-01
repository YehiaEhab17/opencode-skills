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
  .stats-row {
    display: flex;
    justify-content: space-between;
    gap: 15px;
    margin-top: 30px;
  }
  .stat-item {
    flex: 1;
    background: #ffffff;
    padding: 25px 15px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    text-align: center;
    border-bottom: 5px solid var(--secondary);
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  .stat-percent {
    font-size: 2.8em;
    font-weight: 900;
    color: var(--primary);
    line-height: 1;
    margin-bottom: 10px;
    display: block;
    font-family: Impact, sans-serif, system-ui;
    letter-spacing: 1px;
  }
  .stat-percent span {
    font-size: 0.5em;
    color: var(--secondary);
    font-family: 'Segoe UI', system-ui, sans-serif;
    letter-spacing: 0;
  }
  .stat-text {
    font-size: 0.85em;
    color: #555;
    line-height: 1.4;
    margin: 0;
    font-weight: 600;
  }
---

# {{Section Title: e.g. Key Metrics}}

<div class="stats-row">
  <div class="stat-item" style="border-bottom-color: #E74C3C;">
    <span class="stat-percent">{{Number}}<span>%</span></span>
    <p class="stat-text">{{Description of this metric. What it measures.}}</p>
  </div>
  <div class="stat-item" style="border-bottom-color: #F39C12;">
    <span class="stat-percent">{{Number}}<span>%</span></span>
    <p class="stat-text">{{Description of this metric. What it measures.}}</p>
  </div>
  <div class="stat-item" style="border-bottom-color: #3498DB;">
    <span class="stat-percent">{{Number}}<span>%</span></span>
    <p class="stat-text">{{Description of this metric. What it measures.}}</p>
  </div>
  <div class="stat-item" style="border-bottom-color: #2ECC71;">
    <span class="stat-percent">{{Number}}<span>%</span></span>
    <p class="stat-text">{{Description of this metric. What it measures.}}</p>
  </div>
</div>

---

## Stats Row — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.stats-row {
  display: flex;
  justify-content: space-between;
  gap: 15px;
  margin-top: 30px;
}
.stat-item {
  flex: 1;
  background: #ffffff;
  padding: 25px 15px;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.06);
  text-align: center;
  border-bottom: 5px solid var(--secondary);
  display: flex;
  flex-direction: column;
}
.stat-percent {
  font-size: 2.8em;
  font-weight: 900;
  color: var(--primary);
  line-height: 1;
  margin-bottom: 10px;
  display: block;
  font-family: Impact, sans-serif;
  letter-spacing: 1px;
}
.stat-percent span { font-size: 0.5em; color: var(--secondary); }
.stat-text { font-size: 0.85em; color: #555; line-height: 1.4; margin: 0; font-weight: 600; }
```

```html
<div class="stats-row">
  <div class="stat-item" style="border-bottom-color: #E74C3C;">
    <span class="stat-percent">{{Number}}<span>%</span></span>
    <p class="stat-text">{{Description of this metric.}}</p>
  </div>
  <div class="stat-item" style="border-bottom-color: #F39C12;">
    <span class="stat-percent">{{Number}}<span>%</span></span>
    <p class="stat-text">{{Description of this metric.}}</p>
  </div>
  <div class="stat-item" style="border-bottom-color: #3498DB;">
    <span class="stat-percent">{{Number}}<span>%</span></span>
    <p class="stat-text">{{Description of this metric.}}</p>
  </div>
  <div class="stat-item" style="border-bottom-color: #2ECC71;">
    <span class="stat-percent">{{Number}}<span>%</span></span>
    <p class="stat-text">{{Description of this metric.}}</p>
  </div>
</div>
```
