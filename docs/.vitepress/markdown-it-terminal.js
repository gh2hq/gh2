import container from "markdown-it-container";
import {spawnSync} from "child_process";

function codeof(token) {
  if (token.type !== "fence" || token.tag !== "code") throw new Error("missing fenced code block");
  return token.content;
}

export default function terminal(md) {
  md.use(container, "python", {
    render(tokens, idx) {
      // closing tag
      if (tokens[idx].nesting === -1) {
        const token = tokens[idx - 1]; // the code block
        const directives = tokens[idx - 2].info.split(/\s+/).slice(1);
        const content = codeof(token);
        const process = spawnSync("python3", ["-c", content], {encoding: "utf8"});
        const output = process.stdout || process.stderr;
        const safeOutput = md.utils.escapeHtml(output);

        return `<Terminal ${directives.includes("fit") ? "fit" : ""}><pre>\n${safeOutput}</pre></Terminal>`;
      } else {
        // opening tag
        const token = tokens[idx + 1]; // the code block
        const content = codeof(token);
        const link = "https://editor.gh2.dev/#code=" + encodeURIComponent(content);
        return `<a class="gh-open no-icon" target="__blank" href="${link}" title="Run on Oneline Editor">Run</a>`;
      }
    },
  });
}
