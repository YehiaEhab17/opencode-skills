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
  .side-layout {
    display: flex;
    gap: 30px;
    margin-top: 10px;
    align-items: center;
  }
  .side-layout .list-side {
    flex: 1.3;
  }
  .side-layout .img-side {
    flex: 0.7;
    text-align: center;
  }
  .side-layout .img-side img {
    max-height: 380px;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }
---

# {{Slide Title: e.g. How It Works}}

<div class="side-layout">
  <div class="list-side">
    <ol>
      <li><strong>{{Step One}}</strong> {{Brief description of the step.}}</li>
      <li><strong>{{Step Two}}</strong> {{Brief description of the step.}}</li>
      <li><strong>{{Step Three}}</strong> {{Brief description of the step.}}</li>
      <li><strong>{{Step Four}}</strong> {{Brief description of the step.}}</li>
      <li><strong>{{Step Five}}</strong> {{Brief description of the step.}}</li>
    </ol>
  </div>
  <div class="img-side">
    <img src="{{url-to-image}}" alt="{{Image description}}">
  </div>
</div>

---

## Text + Image Side Layout — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.side-layout {
  display: flex;
  gap: 30px;
  margin-top: 10px;
  align-items: center;
}
.side-layout .list-side { flex: 1.3; }
.side-layout .img-side { flex: 0.7; text-align: center; }
.side-layout .img-side img {
  max-height: 380px;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
```

```html
<div class="side-layout">
  <div class="list-side">
    <ol>
      <li><strong>{{Step One}}</strong> {{Brief description.}}</li>
      <li><strong>{{Step Two}}</strong> {{Brief description.}}</li>
      <li><strong>{{Step Three}}</strong> {{Brief description.}}</li>
      <li><strong>{{Step Four}}</strong> {{Brief description.}}</li>
      <li><strong>{{Step Five}}</strong> {{Brief description.}}</li>
    </ol>
  </div>
  <div class="img-side">
    <img src="{{url-to-image}}" alt="{{Image description}}">
  </div>
</div>
```
