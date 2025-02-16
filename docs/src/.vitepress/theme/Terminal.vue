<script setup>
import { useSlots, ref, onMounted } from 'vue';


const { fit } = defineProps(['fit']);
const slots = useSlots();
const output = slots.default()[0].children;
const fixedOutput = output.replace(/\n/g, "\r\n");
const trimEnd = fixedOutput.split("\r\n").slice(0, -1).join("\r\n");
const divRef = ref(null);
const containerRef = ref(null);
const rows = trimEnd.split("\r\n").length;
const cols = Math.max(...trimEnd.split("\r\n").map(line => line.length));

const isFitContent = fit === "";

// Dynamic import
// @xterm/xterm is not ESM, so we need to use dynamic import
// @xterm/addon-fit try to use self
let FitAddon;
let Terminal;

// Render terminal
onMounted(async () => {
  if (!Terminal) Terminal = (await import("@xterm/xterm")).Terminal;

  const container = divRef.value;
  const term = new Terminal({
    ...fit === "" && { cols },
    rows
  });


  if (isFitContent) {
    // Fit content.
    term.open(container);
  } else {
    // Fit container.
    if (!FitAddon) FitAddon = (await import("@xterm/addon-fit")).FitAddon;
    const fitAddon = new FitAddon();
    term.loadAddon(fitAddon);
    term.open(container);
    fitAddon.fit();
  }

  term.write(trimEnd);
  term.write("\x1B[?25l"); // Hide cursor
  return () => term.dispose();
});


// Remove margin bottom of previous element
onMounted(() => {
  const container = containerRef.value;
  const prevElement = container.previousElementSibling;
  if (prevElement) prevElement.style.marginBottom = '0';
});

</script>

<template>
  <div class="container" ref="containerRef">
    <div class="terminal" :style="{ width: isFitContent ? `fit-content` : `` }">
      <div ref="divRef"></div>
    </div>
  </div>
</template>

<style scoped>
.container {
  overflow: auto;
}

.terminal {
  padding: 10px 20px;
  border-radius: 4px;
  background-color: black;
}
</style>