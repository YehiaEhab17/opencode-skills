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
  .quote-container {
    display: flex;
    align-items: center;
    gap: 25px;
    margin-top: 20px;
  }
  .quote-container img {
    width: 130px;
    height: 130px;
    object-fit: cover;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    flex-shrink: 0;
  }
  .quote-container blockquote {
    background: #edf2f7;
    border-left: 8px solid var(--secondary);
    margin: 0;
    padding: 0.8em 1.2em;
    font-style: italic;
    font-size: 0.9em;
    line-height: 1.4;
    border-radius: 4px;
    flex-grow: 1;
  }
  .quote-container blockquote strong {
    color: var(--primary);
  }
---

# {{Section Title: e.g. Testimonial}}

<div class="quote-container">
  <img src="{{image-url}}" alt="{{Image description}}" />
  <blockquote>
    "{{The quote or testimonial text. Keep it impactful and concise.}}"
    <br><strong>— {{Source or author attribution}}</strong>
  </blockquote>
</div>

---

## Quote + Image Container — Template

```css
:root { --primary: #003366; --secondary: #00A8CC; }

.quote-container {
  display: flex;
  align-items: center;
  gap: 25px;
  margin-top: 20px;
}
.quote-container img {
  width: 130px;
  height: 130px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  flex-shrink: 0;
}
.quote-container blockquote {
  background: #edf2f7;
  border-left: 8px solid var(--secondary);
  margin: 0;
  padding: 0.8em 1.2em;
  font-style: italic;
  font-size: 0.9em;
  line-height: 1.4;
  border-radius: 4px;
  flex-grow: 1;
}
.quote-container blockquote strong { color: var(--primary); }
```

```html
<div class="quote-container">
  <img src="{{image-url}}" alt="{{Image description}}" />
  <blockquote>
    "{{The quote or testimonial text.}}"
    <br><strong>— {{Source attribution}}</strong>
  </blockquote>
</div>
```
