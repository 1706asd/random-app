<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>SILICON ARCHITECT // 300mm 반도체 8대 공정 팹 시뮬레이터</title>
<style>
  :root {
    --bg-deep: #050912;
    --bg-panel: #0b1221;
    --bg-card: #101a30;
    --bg-input: #080e1a;
    --border: #1e2f50;
    --border-bright: #2e4b80;
    --cyan: #00f0ff;
    --cyan-dim: rgba(0, 240, 255, 0.14);
    --green: #00e676;
    --green-dim: rgba(0, 230, 118, 0.14);
    --amber: #ffb703;
    --amber-dim: rgba(255, 183, 3, 0.15);
    --red: #ff3b5c;
    --red-dim: rgba(255, 59, 92, 0.15);
    --purple: #b565ff;
    --text-main: #e6eefc;
    --text-sub: #8ba0c4;
    --text-muted: #52678c;
    --font-mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
    --font-sans: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    user-select: none;
  }

  body {
    background-color: var(--bg-deep);
    color: var(--text-main);
    font-family: var(--font-sans);
    height: 100vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }

  /* Top Header Bar */
  header {
    height: 54px;
    background: linear-gradient(90deg, #070d19 0%, #0d172a 50%, #070d19 100%);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    gap: 12px;
    flex-shrink: 0;
  }

  .brand {
    display: flex;
    align-items: center;
    gap: 10px;
    white-space: nowrap;
  }

  .brand-badge {
    background: var(--cyan-dim);
    border: 1px solid var(--cyan);
    color: var(--cyan);
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 700;
    padding: 3px 7px;
    border-radius: 4px;
    letter-spacing: 0.06em;
  }

  .brand-title {
    font-weight: 800;
    font-size: 15px;
    letter-spacing: 0.04em;
    color: #fff;
  }

  .brand-title span {
    color: var(--cyan);
  }

  /* Stage Stepper Bar */
  .stage-nav {
    display: flex;
    align-items: center;
    gap: 4px;
    overflow-x: auto;
    padding: 4px 0;
  }

  .stage-pill {
    background: var(--bg-input);
    border: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 600;
    padding: 5px 9px;
    border-radius: 5px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.18s ease;
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .stage-pill:hover {
    border-color: var(--border-bright);
    color: var(--text-sub);
  }

  .stage-pill.active {
    background: var(--cyan-dim);
    border-color: var(--cyan);
    color: #fff;
    box-shadow: 0 0 12px rgba(0, 240, 255, 0.2);
  }

  .stage-pill.done {
    border-color: rgba(0, 230, 118, 0.45);
    color: var(--green);
  }

  .stage-pill .score-tag {
    font-family: var(--font-mono);
    font-size: 10px;
    background: rgba(0, 230, 118, 0.15);
    padding: 1px 4px;
    border-radius: 3px;
  }

  .header-actions {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
  }

  .icon-btn {
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--text-main);
    font-size: 12px;
    font-weight: 600;
    padding: 6px 11px;
    border-radius: 6px;
    cursor: pointer;
    transition: 0.15s;
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .icon-btn:hover {
    border-color: var(--cyan);
    color: var(--cyan);
  }

  /* Main Workspace */
  .workspace {
    flex: 1;
    display: grid;
    grid-template-columns: 1.75fr 1fr;
    gap: 10px;
    padding: 10px;
    overflow: hidden;
  }

  /* Left Visual Monitors */
  .visual-column {
    display: flex;
    flex-direction: column;
    gap: 10px;
    overflow: hidden;
  }

  .dual-viewports {
    flex: 1;
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 10px;
    min-height: 0;
  }

  .monitor-card {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
  }

  .monitor-header {
    height: 32px;
    background: rgba(16, 26, 48, 0.9);
    border-bottom: 1px solid var(--border);
    padding: 0 12px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 11px;
    font-weight: 700;
    color: var(--text-sub);
    letter-spacing: 0.04em;
    flex-shrink: 0;
  }

  .monitor-header .live-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 8px var(--green);
    margin-right: 6px;
  }

  .monitor-tag {
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--cyan);
    background: var(--cyan-dim);
    padding: 2px 6px;
    border-radius: 3px;
  }

  .canvas-wrap {
    flex: 1;
    position: relative;
    width: 100%;
    height: 100%;
    min-height: 0;
  }

  canvas {
    display: block;
    width: 100%;
    height: 100%;
  }

  /* Bottom Telemetry & Oscilloscope */
  .telemetry-bar {
    height: 175px;
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    overflow: hidden;
    flex-shrink: 0;
  }

  .scope-box {
    display: flex;
    flex-direction: column;
    border-right: 1px solid var(--border);
  }

  .metrics-grid {
    padding: 10px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 8px;
  }

  .metric-tile {
    background: var(--bg-input);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 8px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .metric-label {
    font-size: 10px;
    color: var(--text-sub);
    margin-bottom: 3px;
  }

  .metric-val {
    font-family: var(--font-mono);
    font-size: 15px;
    font-weight: 700;
    color: #fff;
  }

  .metric-sub {
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--text-muted);
    margin-top: 2px;
  }

  /* Right Control Console */
  .control-console {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .console-scroll {
    flex: 1;
    overflow-y: auto;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .console-scroll::-webkit-scrollbar {
    width: 6px;
  }
  .console-scroll::-webkit-scrollbar-thumb {
    background: var(--border-bright);
    border-radius: 3px;
  }

  .stage-title-box {
    border-left: 3px solid var(--cyan);
    padding-left: 10px;
  }

  .stage-kicker {
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--cyan);
    font-weight: 700;
  }

  .stage-heading {
    font-size: 18px;
    font-weight: 800;
    color: #fff;
    margin-top: 2px;
  }

  .stage-desc {
    font-size: 12.5px;
    line-height: 1.55;
    color: var(--text-sub);
    margin-top: 5px;
  }

  .formula-card {
    background: #070c17;
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 9px 12px;
    font-family: var(--font-mono);
    font-size: 11.5px;
    color: var(--amber);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .formula-card span.eq-desc {
    font-family: var(--font-sans);
    font-size: 11px;
    color: var(--text-muted);
  }

  .mission-box {
    background: var(--cyan-dim);
    border: 1px solid rgba(0, 240, 255, 0.35);
    border-radius: 6px;
    padding: 10px 12px;
    font-size: 12px;
    line-height: 1.5;
    color: #dffaff;
  }

  .mission-box strong {
    color: var(--cyan);
    display: block;
    font-size: 11px;
    letter-spacing: 0.04em;
    margin-bottom: 3px;
  }

  /* Controls */
  .control-group {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 11px 12px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .control-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 12px;
    font-weight: 600;
  }

  .control-val {
    font-family: var(--font-mono);
    color: var(--cyan);
    font-size: 12.5px;
  }

  input[type="range"] {
    -webkit-appearance: none;
    width: 100%;
    height: 6px;
    background: var(--bg-input);
    border-radius: 3px;
    border: 1px solid var(--border);
    outline: none;
  }

  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: var(--cyan);
    cursor: pointer;
    box
