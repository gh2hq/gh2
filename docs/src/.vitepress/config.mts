import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "gh2",
  description: "The creative coding language for ASCII art and poetic form",
  appearance: "force-dark",
  cleanUrls: true,
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [{ text: "Examples", link: "/examples" }],

    sidebar: [
      {
        text: "Introduction",
        items: [
          { text: "What is gh2?", link: "/what-is-gh2" },
          { text: "Get Started", link: "/get-started" },
        ],
      },
      {
        text: "Tutorial",
        items: [
          { text: "Hello, Lighght!", link: "/hello-lighght" },
        ],
      },
      { text: "Examples", link: "/examples" },
    ],

    socialLinks: [{ icon: "github", link: "https://github.com/gh2hq/gh2" }],
  },
});
