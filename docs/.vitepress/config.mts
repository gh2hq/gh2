import {defineConfig} from "vitepress";
import terminal from "./markdown-it-terminal.js";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "gh2",
  description: "The creative coding language for ASCII art and poetic form",
  appearance: "force-dark",
  head: [["link", {rel: "icon", type: "image/png", href: "/icon-black.png"}]],
  cleanUrls: true,
  markdown: {
    config: (md) => terminal(md),
  },
  themeConfig: {
    logo: "/icon.svg",
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      {text: "Docs", link: "/docs/what-is-gh2"},
      {text: "Examples", link: "/examples/zeros"},
      {text: "Editor", link: "https://editor.gh2.dev/"},
    ],
    sidebar: {
      "/docs": [
        {
          text: "Introduction",
          items: [
            {text: "What is gh2?", link: "/docs/what-is-gh2"},
            {text: "Get Started", link: "/docs/get-started"},
            {text: "API Index", link: "/docs/api-index"},
          ],
        },
        {
          text: "Tutorial",
          items: [{text: "Hello Lighght", link: "/docs/hello-lighght"}],
        },
      ],
      "/examples": [{text: "Zeros", link: "/examples/zeros"}],
    },
    socialLinks: [{icon: "github", link: "https://github.com/gh2hq/gh2"}],
    footer: {
      message:
        "Library released under <a style='text-decoration:underline;' href='https://github.com/gh2hq/gh2/blob/main/LICENSE'>ISC License</a>.",
      copyright: `Copyright 2020–${new Date().getUTCFullYear()} Bairui Su.`,
    },
  },
});
