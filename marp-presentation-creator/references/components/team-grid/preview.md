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
  .team-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
    margin-top: 10px;
  }
  .team-card {
    background: #ffffff;
    padding: 15px 10px;
    text-align: center;
    border-radius: 10px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.05);
    border-bottom: 4px solid var(--secondary);
  }
  .team-card h4 {
    margin: 0 0 5px 0;
    color: var(--primary);
    font-size: 0.9em;
  }
  .team-card p {
    margin: 0;
    font-size: 0.75em;
    color: #7f8c8d;
    font-weight: 500;
  }
  .team-icon {
    font-size: 2em;
    margin-bottom: 10px;
  }
---

# {{Section Title: e.g. Meet The Team}}

<div class="team-grid">
  <div class="team-card">
    <div class="team-icon">{{Icon}}</div>
    <h4>{{Person One Name}}</h4>
    <p>{{Role or Title}}</p>
  </div>
  <div class="team-card">
    <div class="team-icon">{{Icon}}</div>
    <h4>{{Person Two Name}}</h4>
    <p>{{Role or Title}}</p>
  </div>
  <div class="team-card">
    <div class="team-icon">{{Icon}}</div>
    <h4>{{Person Three Name}}</h4>
    <p>{{Role or Title}}</p>
  </div>
  <div class="team-card">
    <div class="team-icon">{{Icon}}</div>
    <h4>{{Person Four Name}}</h4>
    <p>{{Role or Title}}</p>
  </div>
</div>

---

## Team Grid — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.team-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 15px;
  margin-top: 10px;
}
.team-card {
  background: #ffffff;
  padding: 15px 10px;
  text-align: center;
  border-radius: 10px;
  box-shadow: 0 6px 15px rgba(0,0,0,0.05);
  border-bottom: 4px solid var(--secondary);
}
.team-card h4 { margin: 0 0 5px 0; color: var(--primary); font-size: 0.9em; }
.team-card p { margin: 0; font-size: 0.75em; color: #7f8c8d; font-weight: 500; }
.team-icon { font-size: 2em; margin-bottom: 10px; }
```

```html
<div class="team-grid">
  <div class="team-card">
    <div class="team-icon">{{Icon}}</div>
    <h4>{{Person One Name}}</h4>
    <p>{{Role or Title}}</p>
  </div>
  <div class="team-card">
    <div class="team-icon">{{Icon}}</div>
    <h4>{{Person Two Name}}</h4>
    <p>{{Role or Title}}</p>
  </div>
  <div class="team-card">
    <div class="team-icon">{{Icon}}</div>
    <h4>{{Person Three Name}}</h4>
    <p>{{Role or Title}}</p>
  </div>
  <div class="team-card">
    <div class="team-icon">{{Icon}}</div>
    <h4>{{Person Four Name}}</h4>
    <p>{{Role or Title}}</p>
  </div>
</div>
```
