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
  .timeline {
    display: flex;
    gap: 15px;
    margin-top: 20px;
  }
  .step {
    flex: 1;
    background: #ffffff;
    padding: 20px 15px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    border-top: 6px solid var(--secondary);
    text-align: center;
    position: relative;
  }
  .step-num {
    display: inline-block;
    width: 35px;
    height: 35px;
    background: var(--primary);
    color: white;
    border-radius: 50%;
    line-height: 35px;
    font-weight: bold;
    font-size: 1.1em;
    margin-bottom: 10px;
    box-shadow: 0 4px 10px rgba(0,51,102,0.3);
  }
  .step h3 {
    color: var(--primary);
    font-size: 1em;
    margin: 0 0 8px 0;
  }
  .step p {
    font-size: 0.8em;
    margin: 0;
    color: #555;
    line-height: 1.3;
  }
  .step::after {
    content: '\279E';
    position: absolute;
    right: -18px;
    top: 40%;
    font-size: 1.5em;
    color: var(--secondary);
    z-index: 100;
  }
  .step:last-child::after {
    display: none;
  }

  .template-section {
    margin-top: 30px;
    background: #1e1e1e;
    color: #d4d4d4;
    padding: 20px;
    border-radius: 8px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 0.55em;
    line-height: 1.5;
    white-space: pre-wrap;
  }
---

# {{Phase Title}}

A brief introductory sentence describing the overall plan or roadmap.

<div class="timeline">
  <div class="step">
    <div class="step-num">1</div>
    <h3>{{Step One Name}}</h3>
    <p>{{Brief description of what happens in this phase or step.}}</p>
  </div>
  <div class="step">
    <div class="step-num">2</div>
    <h3>{{Step Two Name}}</h3>
    <p>{{Brief description of what happens in this phase or step.}}</p>
  </div>
  <div class="step">
    <div class="step-num">3</div>
    <h3>{{Step Three Name}}</h3>
    <p>{{Brief description of what happens in this phase or step.}}</p>
  </div>
</div>

---

## Process Timeline — Template

```css
/* Copy this into your presentation's <style> block */
:root { --primary: #003366; --secondary: #00A8CC; }

.timeline {
  display: flex;
  gap: 15px;
  margin-top: 20px;
}
.step {
  flex: 1;
  background: #ffffff;
  padding: 20px 15px;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.06);
  border-top: 6px solid var(--secondary);
  text-align: center;
  position: relative;
}
.step-num {
  display: inline-block;
  width: 35px; height: 35px;
  background: var(--primary);
  color: white;
  border-radius: 50%;
  line-height: 35px;
  font-weight: bold;
  font-size: 1.1em;
  margin-bottom: 10px;
  box-shadow: 0 4px 10px rgba(0,51,102,0.3);
}
.step h3 {
  color: var(--primary);
  font-size: 1em;
  margin: 0 0 8px 0;
}
.step p {
  font-size: 0.8em;
  margin: 0;
  color: #555;
  line-height: 1.3;
}
.step::after {
  content: '\279E';
  position: absolute;
  right: -18px;
  top: 40%;
  font-size: 1.5em;
  color: var(--secondary);
}
.step:last-child::after { display: none; }
```

```html
<div class="timeline">
  <div class="step">
    <div class="step-num">1</div>
    <h3>{{Step One Name}}</h3>
    <p>{{Brief description of what happens in this phase or step.}}</p>
  </div>
  <div class="step">
    <div class="step-num">2</div>
    <h3>{{Step Two Name}}</h3>
    <p>{{Brief description of what happens in this phase or step.}}</p>
  </div>
  <div class="step">
    <div class="step-num">3</div>
    <h3>{{Step Three Name}}</h3>
    <p>{{Brief description of what happens in this phase or step.}}</p>
  </div>
</div>
```
