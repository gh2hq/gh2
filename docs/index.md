---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "gh2"
  text: "A Python library for creative ASCII art and poetic form"
  tagline: Create computational letterforms in the P5 style or explore the most fun way to learn Python
  image:
    src: /example.png
    alt: gh2-example
  actions:
    - theme: brand
      text: Get Started
      link: /docs/get-started
    - theme: alt
      text: What is gh2?
      link: /docs/what-is-gh2
    - theme: alt
      text: Examples
      link: /examples/zeros

features:
  - title: Customizable Margins
    details: Adjust top, bottom, and left margins for the generated art
  - title: Glyph Placement
    details: Place specific characters at coordinates within grid to form artwork
  - title: Rendering
    details: Stores art into string or prints to console based on margins and gylphs provided
---

<div id="hero-name" style="display:none">
  <img src="/logo.svg" style="padding-bottom:20px"/>
</div>

<script setup>

import {onMounted} from "vue";

onMounted(() => {
  const p = document.querySelector(".name.clip");
  const s = document.querySelector("#hero-name");
  if (!p || !s) return;
  while (p.lastChild) p.lastChild.remove();
  s.style.display = "block";
  p.append(s);
});

</script>

<style>

.VPHero .text {
  font-size: 45px !important;
  line-height: 56px !important;
}

.VPImage.image-src {
  border-radius: 10px;
}
</style>
