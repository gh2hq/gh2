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
      link: /get-started
    - theme: alt
      text: What is gh2?
      link: /what-is-gh2

features:
  - title: Feature A
    details: Lorem ipsum dolor sit amet, consectetur adipiscing elit
  - title: Feature B
    details: Lorem ipsum dolor sit amet, consectetur adipiscing elit
  - title: Feature C
    details: Lorem ipsum dolor sit amet, consectetur adipiscing elit
---

<div id="hero-name">
  <img src="/logo.svg" style="padding-bottom:20px"/>
</div>

<script setup>

import {onMounted} from "vue";

onMounted(() => {
  const p = document.querySelector(".name.clip");
  const s = document.querySelector("#hero-name");
  if (!p || !s) return;
  while (p.lastChild) p.lastChild.remove();
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
