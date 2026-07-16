const POLL_INTERVAL_MS = 3000;
let snapshot = JSON.stringify(window.ARGOS_DATA);

function poll() {
  const script = document.createElement("script");
  script.src = "data.js";
  script.onload = () => {
    script.remove();
    const next = JSON.stringify(window.ARGOS_DATA);
    if (next !== snapshot) {
      snapshot = next;
      document.dispatchEvent(
        new CustomEvent("argos:data-changed", {
          detail: window.ARGOS_DATA,
        }),
      );
    }
  };
  document.head.appendChild(script);
}

setInterval(poll, POLL_INTERVAL_MS);
