# -*- coding: utf-8 -*-
import os

target_path = r"C:\Users\User\.gemini\antigravity\scratch\higiene-del-sueno-sst\index.html"

html_code = r'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>Herramienta SST • Hábitos de Sueño y Descompresión | ISAVAL SG-SST</title>
  <meta name="description" content="Plataforma de higiene y hábitos de sueño para trabajadores SST: cerebro 3D interactivo para mirar por dentro, biomecánica pulmonar 4-7-8 con apnea real, simulador de conducción realista y comparativa biomédica.">
  <meta name="theme-color" content="#eef2f6">

  <style>
    /* =========================================================================
       1. VARIABLES Y DISEÑO PROFESIONAL CON FONDO CLARO SUAVE (#eef2f6)
       ========================================================================= */
    :root {
      --bg-base: #eef2f6;
      --bg-surface: #ffffff;
      --bg-surface-subtle: #f8fafc;
      --border-subtle: #e2e8f0;
      --border-focus: #0284c7;

      --cyan-brand: #0284c7;
      --cyan-light: #e0f2fe;
      --indigo-brand: #4f46e5;
      --gold-accent: #d97706;
      --amber-alert: #ea580c;
      --red-alert: #dc2626;
      --emerald-safe: #059669;

      --text-title: #0f172a;
      --text-body: #334155;
      --text-muted: #64748b;
      --text-light: #94a3b8;

      --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", "Helvetica Neue", sans-serif;
      --radius-pill: 9999px;
      --radius-card: 18px;
      --radius-sm: 10px;
      --shadow-card: 0 10px 25px -5px rgba(15, 23, 42, 0.08), 0 8px 10px -6px rgba(15, 23, 42, 0.04);
      --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
    }

    html, body {
      width: 100%;
      height: 100%;
      overflow: hidden;
      background-color: #f0f4f9;
      background-image:
        radial-gradient(ellipse 65% 55% at 5% 5%, rgba(2, 132, 199, 0.09) 0%, transparent 65%),
        radial-gradient(ellipse 60% 50% at 95% 8%, rgba(79, 70, 229, 0.08) 0%, transparent 65%),
        radial-gradient(ellipse 65% 55% at 90% 92%, rgba(5, 150, 105, 0.06) 0%, transparent 65%),
        radial-gradient(ellipse 50% 50% at 50% 50%, rgba(255, 255, 255, 0.60) 0%, transparent 75%),
        radial-gradient(rgba(148, 163, 184, 0.32) 1.1px, transparent 1.1px);
      background-size: 100% 100%, 100% 100%, 100% 100%, 100% 100%, 28px 28px;
      background-position: 0 0, 0 0, 0 0, 0 0, 0 0;
      background-attachment: fixed;
      font-family: var(--font-stack);
      color: var(--text-body);
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    #antigravity-particles-canvas {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }

    /* =========================================================================
       2. CABECERA INSTITUCIONAL CON LOGOS AUTÉNTICOS (ISAVAL)
       ========================================================================= */
    .antigravity-nav-header {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 64px;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 28px;
      z-index: 1000;
      box-shadow: 0 2px 10px rgba(15, 23, 42, 0.03);
    }

    .nav-brand-pill {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .nav-corp-logo {
      height: 38px;
      max-width: 130px;
      object-fit: contain;
      filter: drop-shadow(0 1px 3px rgba(0,0,0,0.06));
    }

    .nav-separator-line {
      width: 1px;
      height: 28px;
      background-color: var(--border-subtle);
    }

    .nav-program-title {
      font-size: 0.84rem;
      font-weight: 800;
      color: var(--text-title);
      letter-spacing: 0.03em;
      text-transform: uppercase;
    }

    .nav-program-subtitle {
      font-size: 0.68rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .stages-stepper-row {
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-surface-subtle);
      padding: 4px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--border-subtle);
    }

    .stage-step-pill {
      background: transparent;
      border: none;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      transition: var(--transition);
      letter-spacing: 0.02em;
    }

    .stage-step-pill:hover {
      color: var(--text-title);
      background: rgba(2, 132, 199, 0.08);
    }

    .stage-step-pill.is-active {
      background: #FFFFFF;
      color: var(--cyan-brand);
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.08);
      font-weight: 800;
    }

    /* =========================================================================
       3. CONTENEDOR PRINCIPAL DE FASES
       ========================================================================= */
    .main-stages-viewport {
      position: absolute;
      top: 126px;
      bottom: 60px;
      left: 0;
      right: 0;
      overflow: hidden;
      overflow-x: hidden;
      z-index: 10;
    }

    .stage-layer {
      position: absolute;
      inset: 0;
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transition: opacity 0.4s ease, transform 0.4s ease;
      transform: scale(0.985);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    .stage-layer.is-active {
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
      transform: scale(1);
    }

    /* =========================================================================
       4. BOT CEREBRITO SST Y NARRACIÓN
       ========================================================================= */
        /* =========================================================================
       4. BANNER COPILOTO ASISTENTE SOMNIBOT SG-SST (100% LIBRE DE SUPERPOSICIÓN)
       ========================================================================= */
    .somnibot-copilot-banner {
      position: fixed;
      top: 72px;
      left: 50%;
      transform: translateX(-50%);
      width: calc(100% - 48px);
      max-width: 1440px;
      min-height: 60px;
      height: auto;
      padding: 10px 22px;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      box-shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
      display: flex;
      align-items: center;
      gap: 16px;
      z-index: 100;
      box-sizing: border-box;
      transition: var(--transition);
    }

    .somnibot-banner-avatar-wrap {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 2px solid var(--cyan-brand);
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      flex-shrink: 0;
      cursor: pointer;
      transition: var(--transition);
    }

    .somnibot-banner-avatar-wrap:hover {
      transform: scale(1.06);
      border-color: var(--navy-corp);
    }

    .somnibot-banner-avatar-img {
      width: 82%;
      height: 82%;
      object-fit: contain;
    }

    .somnibot-pulse-ring {
      position: absolute;
      inset: -3px;
      border-radius: 50%;
      border: 2px solid var(--cyan-brand);
      opacity: 0.6;
      animation: botPulse 2.4s infinite cubic-bezier(0.25, 1, 0.5, 1);
    }

    @keyframes botPulse {
      0% { transform: scale(0.95); opacity: 0.8; }
      70% { transform: scale(1.22); opacity: 0; }
      100% { transform: scale(1.22); opacity: 0; }
    }

    .somnibot-banner-body {
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
      gap: 5px;
    }

    .somnibot-banner-tagline {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .somnibot-banner-tag {
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.06em;
      color: var(--cyan-brand);
      text-transform: uppercase;
    }

    .somnibot-banner-voice-btn {
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: 12px;
      padding: 1px 8px;
      font-size: 10px;
      font-weight: 700;
      color: var(--emerald-safe);
      display: inline-flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      transition: var(--transition);
    }

    .somnibot-banner-voice-btn:hover {
      background: rgba(16, 185, 129, 0.2);
    }

    .somnibot-banner-voice-btn.is-muted {
      background: rgba(100, 116, 139, 0.1);
      border-color: rgba(100, 116, 139, 0.25);
      color: var(--text-muted);
    }

    .somnibot-banner-text {
      font-size: 13.5px;
      color: var(--text-title);
      line-height: 1.55;
      font-weight: 500;
      letter-spacing: 0.012em;
    }

    .somnibot-banner-right {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }

    .somnibot-eq-bars {
      display: flex;
      align-items: flex-end;
      gap: 3px;
      height: 18px;
      padding: 0 4px;
    }

    .somnibot-eq-bar {
      width: 3px;
      background: var(--cyan-brand);
      border-radius: 2px;
      height: 5px;
      transition: height 0.2s ease;
    }

    .somnibot-eq-bars.is-speaking .somnibot-eq-bar:nth-child(1) {
      animation: eqBounce 0.8s infinite ease-in-out;
    }
    .somnibot-eq-bars.is-speaking .somnibot-eq-bar:nth-child(2) {
      animation: eqBounce 0.8s infinite 0.2s ease-in-out;
    }
    .somnibot-eq-bars.is-speaking .somnibot-eq-bar:nth-child(3) {
      animation: eqBounce 0.8s infinite 0.4s ease-in-out;
    }
    .somnibot-eq-bars.is-speaking .somnibot-eq-bar:nth-child(4) {
      animation: eqBounce 0.8s infinite 0.15s ease-in-out;
    }

    @keyframes eqBounce {
      0%, 100% { height: 4px; }
      50% { height: 16px; }
    }

    .antigravity-bottom-dock {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 60px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(12px);
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 28px;
      z-index: 1000;
    }

    .dock-stage-counter {
      font-size: 0.76rem;
      font-weight: 800;
      color: var(--text-muted);
      letter-spacing: 0.04em;
    }

    .dock-nav-btns {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .dock-btn {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      color: var(--text-title);
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      font-size: 0.76rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .dock-btn:hover {
      background: var(--bg-surface-subtle);
      border-color: var(--cyan-brand);
      color: var(--cyan-brand);
    }

    .dock-btn.is-primary {
      background: var(--cyan-brand);
      border-color: var(--cyan-brand);
      color: #FFFFFF;
    }

    .dock-btn.is-primary:hover {
      background: #0369a1;
      border-color: #0369a1;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
    }

    /* =========================================================================
       5. FASE 1: CEREBRO ANATÓMICO 3D INTERACTIVO (MIRAR POR DENTRO Y ROTAR)
       ========================================================================= */
    #stage-brain-full {
      width: 100%;
      max-width: 1440px;
      height: 100%;
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 24px;
      align-items: stretch;
      max-height: calc(100vh - 210px);
    }

    .brain-intro-panel {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-card);
      padding: 32px 34px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .hero-eyebrow {
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--gold-accent);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 8px;
    }

    .hero-h1 {
      font-size: 1.95rem;
      font-weight: 900;
      color: var(--text-title);
      line-height: 1.2;
      margin-bottom: 14px;
      letter-spacing: -0.02em;
    }

    .hero-desc {
      font-size: 0.88rem;
      color: var(--text-body);
      line-height: 1.6;
      margin-bottom: 20px;
    }

    .intro-pillars-box {
      background: var(--bg-surface-subtle);
      border-left: 3px solid var(--cyan-brand);
      padding: 14px 16px;
      border-radius: 8px;
      font-size: 0.80rem;
      color: var(--text-body);
      line-height: 1.5;
      margin-bottom: 24px;
    }

    .intro-actions-row {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .hero-cta-btn {
      background: var(--cyan-brand);
      color: #FFFFFF;
      border: none;
      padding: 12px 24px;
      border-radius: var(--radius-pill);
      font-size: 0.82rem;
      font-weight: 800;
      cursor: pointer;
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.28);
    }

    .hero-cta-btn:hover {
      background: #0369a1;
      transform: translateY(-1px);
    }

    .hero-sec-btn {
      background: #FFFFFF;
      color: var(--text-title);
      border: 1px solid var(--border-subtle);
      padding: 12px 20px;
      border-radius: var(--radius-pill);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--transition);
    }

    .hero-sec-btn:hover {
      background: var(--bg-surface-subtle);
      border-color: var(--border-focus);
    }

    /* Contenedor del cerebro 3D: Tarjeta blanca impecable, perfectamente integrada */
    .brain-canvas-container {
      position: relative;
      width: 100%;
      height: 100%;
      min-height: 520px;
      max-height: calc(100vh - 210px);
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-card);
      box-shadow: var(--shadow-card);
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      cursor: grab;
    }

    .brain-canvas-container:active {
      cursor: grabbing;
    }

    #anatomical-brain-canvas {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      display: block;
    }

    /* Barra superior de la RUTA GUIADA del Cerebro 3D */
    .brain-tour-dock {
      position: absolute;
      top: 14px;
      left: 14px;
      right: 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      pointer-events: none;
      z-index: 10;
      gap: 12px;
      flex-wrap: nowrap;
    }

    .btour-header-group {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      padding: 4px 10px;
      pointer-events: auto;
      box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
      flex-shrink: 1;
      min-width: 0;
      overflow: hidden;
    }

    .btour-badge {
      font-size: 0.62rem;
      font-weight: 900;
      color: var(--cyan-brand);
      background: rgba(2, 132, 199, 0.08);
      border: 1px solid rgba(2, 132, 199, 0.2);
      border-radius: var(--radius-pill);
      padding: 3px 8px;
      letter-spacing: 0.06em;
      white-space: nowrap;
      flex-shrink: 0;
    }

    .btour-steps-stepper {
      display: flex;
      align-items: center;
      gap: 3px;
      min-width: 0;
      overflow: hidden;
    }

    .pill-short { display: none; }
    .bstep-short { display: inline; }
    .bstep-full { display: none; }

    @media (min-width: 1540px) {
      .bstep-short { display: none; }
      .bstep-full { display: inline; }
    }

    @media (max-width: 980px) {
      .pill-full { display: none; }
      .pill-short { display: inline; }
    }

    .btour-step-btn {
      background: transparent;
      border: 1px solid transparent;
      padding: 4px 8px;
      border-radius: var(--radius-pill);
      font-size: 0.68rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 4px;
      white-space: nowrap;
      height: 28px;
    }

    .btour-step-btn:hover {
      background: rgba(2, 132, 199, 0.06);
      color: var(--text-title);
    }

    .btour-step-btn.is-active {
      background: var(--cyan-brand);
      color: #FFFFFF;
      font-weight: 800;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.25);
    }

    .btour-step-btn.is-active.is-step-stress {
      background: var(--red-alert);
      box-shadow: 0 2px 8px rgba(220, 38, 38, 0.25);
    }

    .bstep-num {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.08);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.62rem;
      font-weight: 900;
      flex-shrink: 0;
    }

    .btour-step-btn.is-active .bstep-num {
      background: rgba(255, 255, 255, 0.25);
      color: #FFFFFF;
    }

    .bstep-sep {
      color: var(--text-light);
      font-size: 0.62rem;
      font-weight: 900;
      flex-shrink: 0;
    }

    /* CONTROLES GUIADOS: DISEÑO PILL UNIFICADO, ELEGANTE Y COMPLETO */
    .btour-controls-group {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      padding: 4px 6px;
      pointer-events: auto;
      box-shadow: 0 4px 14px rgba(15, 23, 42, 0.08);
      flex-shrink: 0;
    }

    .btour-ctrl-btn {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      padding: 4px 12px;
      border-radius: var(--radius-pill);
      font-size: 0.70rem;
      font-weight: 800;
      color: #334155;
      cursor: pointer;
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
      height: 30px;
      box-sizing: border-box;
      line-height: 1;
    }

    .btour-ctrl-btn:hover {
      background: #FFFFFF;
      border-color: var(--cyan-brand);
      color: var(--cyan-brand);
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.15);
      transform: translateY(-1px);
    }

    .btour-ctrl-btn.is-play-pause {
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #FFFFFF;
      border: 1px solid #0284c7;
      font-weight: 900;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.25);
    }

    .btour-ctrl-btn.is-play-pause:hover {
      background: linear-gradient(135deg, #0369a1, #075985);
      color: #FFFFFF;
      border-color: #0369a1;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.35);
      transform: translateY(-1px);
    }

    .btour-ctrl-btn:disabled,
    .btour-ctrl-btn.is-disabled {
      opacity: 0.45;
      cursor: not-allowed;
      pointer-events: none;
      background: rgba(241, 245, 249, 0.6);
      border-color: #E2E8F0;
      color: #94A3B8;
      box-shadow: none;
      transform: none;
    }

    .brain-telemetry-dock {
      position: absolute;
      bottom: 12px;
      left: 14px;
      right: 14px;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 8px 16px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      z-index: 10;
      box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
      pointer-events: auto;
    }

    .telemetry-item {
      display: flex;
      flex-direction: column;
    }

    .telemetry-lbl {
      font-size: 0.62rem;
      font-weight: 800;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .telemetry-val {
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--text-title);
      font-family: monospace;
    }

    /* =========================================================================
       6. FASE 2: BIOMECÁNICA PULMONAR 4-7-8 CON DETENCIÓN TOTAL (APNEA 7s)
       ========================================================================= */
    #stage-breathing-full {
      width: 100%;
      max-width: 1240px;
      height: 100%;
      display: grid;
      grid-template-columns: 420px 1fr;
      gap: 28px;
      align-items: center;
    }

    .resp-cycle-pills-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin: 8px 0 12px 0;
      flex-wrap: wrap;
    }
    .rc-pill {
      background: rgba(6, 182, 212, 0.1);
      border: 1px solid rgba(6, 182, 212, 0.3);
      color: var(--cyan-brand);
      font-size: 0.84rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 8px;
    }
    .rc-arrow {
      color: var(--text-muted);
      font-weight: 800;
      font-size: 0.85rem;
    }

    .breathing-side-panel {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-card);
      padding: 32px 34px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .resp-badge-top {
      display: inline-block;
      align-self: flex-start;
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--cyan-brand);
      background: var(--cyan-light);
      padding: 4px 12px;
      border-radius: var(--radius-pill);
      margin-bottom: 12px;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }

    .resp-phase-giant {
      font-size: 2.8rem;
      font-weight: 900;
      letter-spacing: -0.02em;
      color: var(--text-title);
      line-height: 1.1;
      margin-bottom: 4px;
      transition: color 0.3s ease;
    }

    .resp-counter-giant {
      font-size: 4.8rem;
      font-weight: 900;
      color: var(--cyan-brand);
      font-family: monospace;
      line-height: 1;
      margin-bottom: 12px;
      transition: color 0.3s ease;
    }

    .resp-instructions-text {
      font-size: 0.86rem;
      color: var(--text-body);
      line-height: 1.55;
      margin-bottom: 16px;
    }

    .resp-mechanics-card {
      background: var(--bg-surface-subtle);
      border-left: 3px solid var(--gold-accent);
      padding: 10px 14px;
      border-radius: 6px;
      margin-bottom: 22px;
    }

    .resp-mechanics-title {
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--gold-accent);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 3px;
    }

    .resp-mechanics-desc {
      font-size: 0.76rem;
      color: var(--text-body);
      line-height: 1.4;
    }

    .resp-control-buttons-row {
      display: flex;
      gap: 10px;
    }

    .breathing-canvas-container {
      position: relative;
      width: 100%;
      height: 100%;
      min-height: 520px;
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-card);
      box-shadow: var(--shadow-card);
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }

    #breath-rings-canvas {
      width: 100%;
      height: 100%;
      display: block;
    }

    .breath-hud-hold-pill {
      position: absolute;
      top: 20px;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid var(--emerald-safe);
      color: var(--emerald-safe);
      padding: 6px 16px;
      border-radius: var(--radius-pill);
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      display: none;
      animation: pulseHold 1s infinite alternate;
      z-index: 10;
    }

    .breath-hud-hold-pill.is-active {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    @keyframes pulseHold {
      from { transform: scale(1); opacity: 0.85; }
      to { transform: scale(1.05); opacity: 1; }
    }

    /* =========================================================================
       7. FASE 3: SIMULADOR VIAL POV PROCEDURAL Y REALISTA (ANIMACIÓN ACTIVA)
       ========================================================================= */
    #stage-truck-full {
      position: relative;
      width: 100%;
      height: 100%;
      background: #020617;
      overflow: hidden;
      border-radius: var(--radius-card);
      box-shadow: var(--shadow-card);
    }

    #truck-full-canvas {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      display: block;
      z-index: 2;
    }

    /* Párpados que caen con caída progresiva */
    .eyelid-full-top, .eyelid-full-bottom {
      position: absolute;
      left: 0;
      right: 0;
      background: #000000;
      pointer-events: none;
      z-index: 40;
      transition: height 0.35s ease;
    }

    .eyelid-full-top {
      top: 0;
      height: 0%;
      border-bottom: 4px solid rgba(220, 38, 38, 0.6);
    }

    .eyelid-full-bottom {
      bottom: 0;
      height: 0%;
      border-top: 4px solid rgba(220, 38, 38, 0.6);
    }

    .truck-full-blackout {
      position: absolute;
      inset: 0;
      background: #000000;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 50;
      color: #FFFFFF;
      text-align: center;
      padding: 30px;
    }

    .truck-full-blackout.is-active {
      display: flex;
    }

    .truck-full-crash {
      position: absolute;
      inset: 0;
      background: rgba(185, 28, 28, 0.95);
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 60;
      color: #FFFFFF;
      text-align: center;
      padding: 40px;
    }

    .truck-full-crash.is-active {
      display: flex;
      animation: screenCrashShake 0.45s ease;
    }

    @keyframes screenCrashShake {
      0%, 100% { transform: translate(0, 0); }
      20% { transform: translate(-14px, 10px); }
      40% { transform: translate(14px, -10px); }
      60% { transform: translate(-10px, -8px); }
      80% { transform: translate(10px, 8px); }
    }

    /* Controles de la cabina */
    .truck-full-controls-dock {
      position: absolute;
      bottom: 24px;
      right: 28px;
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(15, 23, 42, 0.92);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: var(--radius-pill);
      padding: 8px 20px;
      z-index: 30;
      box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    }

    .truck-btn-pill {
      background: #FFFFFF;
      color: #0f172a;
      border: none;
      border-radius: var(--radius-pill);
      padding: 9px 18px;
      font-size: 0.74rem;
      font-weight: 800;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .truck-btn-pill:hover {
      background: #f1f5f9;
      transform: translateY(-1px);
    }

    .truck-btn-pill.danger {
      background: var(--red-alert);
      color: #FFFFFF;
    }

    .truck-btn-pill.danger:hover {
      background: #b91c1c;
    }

    .truck-fatigue-hud-pill {
      display: flex;
      align-items: center;
      gap: 10px;
      color: #FFFFFF;
      font-size: 0.72rem;
      font-weight: 800;
      border-left: 1px solid rgba(255, 255, 255, 0.20);
      padding-left: 14px;
    }

    .tf-track {
      width: 80px;
      height: 7px;
      background: rgba(255, 255, 255, 0.25);
      border-radius: var(--radius-pill);
      overflow: hidden;
    }

    .tf-fill {
      width: 0%;
      height: 100%;
      background: var(--emerald-safe);
      transition: width 0.3s ease, background-color 0.3s ease;
    }

    /* =========================================================================
       8. FASE 4: DECISIONES DE TURNO
       ========================================================================= */
    #stage-dilemmas-full {
      width: 100%;
      max-width: 1360px;
      height: 100%;
      display: grid;
      grid-template-columns: 460px 1fr;
      gap: 24px;
      align-items: center;
    }

    .dilemma-brain-stage {
      width: 100%;
      height: 100%;
      min-height: 540px;
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-card);
      box-shadow: var(--shadow-card);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 18px;
    }

    .dil-brain-top-tag {
      position: relative;
      z-index: 10;
      align-self: center;
      background: rgba(241, 245, 249, 0.95);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      padding: 5px 14px;
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--cyan-brand);
      letter-spacing: 0.05em;
      text-transform: uppercase;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    .dil-brain-bottom-telemetry {
      position: relative;
      z-index: 10;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 8px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--text-muted);
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
    }

    #dilemma-brain-canvas {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      display: block;
    }

    .dilemma-content-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-card);
      padding: 34px 38px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .dilemma-step-header {
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--cyan-brand);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 8px;
    }

    .dilemma-title-h2 {
      font-size: 1.55rem;
      font-weight: 900;
      color: var(--text-title);
      margin-bottom: 12px;
      line-height: 1.25;
      letter-spacing: -0.01em;
    }

    .dilemma-desc-p {
      font-size: 0.86rem;
      color: var(--text-body);
      line-height: 1.55;
      margin-bottom: 22px;
    }

    .dilemma-choices-container {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .neutral-choice-card {
      background: var(--bg-surface-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 16px 20px;
      text-align: left;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: flex-start;
      gap: 14px;
    }

    .neutral-choice-card:hover {
      background: #FFFFFF;
      border-color: var(--cyan-brand);
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.08);
      transform: translateY(-1px);
    }

    .neutral-choice-card.is-chosen-good {
      background: #f0fdf4;
      border-color: var(--emerald-safe);
    }

    .neutral-choice-card.is-chosen-bad {
      background: #fef2f2;
      border-color: var(--red-alert);
    }

    .choice-tag {
      font-size: 0.66rem;
      font-weight: 800;
      color: var(--text-muted);
      background: #FFFFFF;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--border-subtle);
      white-space: nowrap;
    }

    .choice-body-text {
      font-size: 0.82rem;
      color: var(--text-title);
      font-weight: 600;
      line-height: 1.45;
    }

    .dilemma-explanation-box {
      margin-top: 18px;
      padding: 14px 18px;
      border-radius: 10px;
      font-size: 0.82rem;
      line-height: 1.5;
      display: none;
    }

    .dilemma-explanation-box.is-active {
      display: block;
    }

    .dilemma-explanation-box.good {
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }

    .dilemma-explanation-box.bad {
      background: #fef2f2;
      border: 1px solid #fecaca;
      color: #991b1b;
    }

    /* =========================================================================
       9. FASE 5: FISIOLOGÍA DEL ESTRÉS Y EL SUEÑO • NEUROBIOLOGÍA CLÍNICA
       ========================================================================= */
    #stage-stress-full {
      width: 100%;
      max-width: 1400px;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .stress-header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }

    .stress-quick-toggle-bar {
      display: flex;
      gap: 10px;
    }

    .stress-toggle-btn {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      padding: 7px 16px;
      border-radius: var(--radius-pill);
      font-size: 0.76rem;
      font-weight: 800;
      color: var(--text-muted);
      cursor: pointer;
      transition: var(--transition);
      box-shadow: var(--shadow-sm);
    }

    .stress-toggle-btn:hover {
      border-color: var(--cyan-brand);
      color: var(--cyan-brand);
    }

    .stress-toggle-btn.is-active#btn-stress-mode-alert {
      background: rgba(239, 68, 68, 0.08);
      border-color: var(--red-alert);
      color: var(--red-alert);
      box-shadow: 0 0 12px rgba(239, 68, 68, 0.2);
    }

    .stress-toggle-btn.is-active#btn-stress-mode-calm {
      background: rgba(16, 185, 129, 0.08);
      border-color: var(--emerald-safe);
      color: var(--emerald-safe);
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.2);
    }

    .stress-layout-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      align-items: stretch;
    }

    /* COLUMNA 1: DIBUJO ANATÓMICO Y BIOCIRCUITO DEL EJE ESTRÉS-SUEÑO */
    .stress-anatomy-art-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-card);
      padding: 16px 18px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 10px;
    }

    .bio-circuit-badge-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .bio-circuit-badge {
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.06em;
      color: var(--text-muted);
      text-transform: uppercase;
    }

    .bio-status-pill {
      font-size: 0.64rem;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 9999px;
      text-transform: uppercase;
    }
    .bio-status-pill.alert {
      background: rgba(239, 68, 68, 0.12);
      color: var(--red-alert);
    }
    .bio-status-pill.calm {
      background: rgba(16, 185, 129, 0.12);
      color: var(--emerald-safe);
    }

    /* Contenedor del SVG Anatómico */
    .bio-anatomy-svg-wrapper {
      width: 100%;
      position: relative;
      background: #F8FAFC;
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .bio-anatomy-svg-wrapper svg {
      width: 100%;
      height: auto;
      max-height: 345px;
      display: block;
    }

    /* Animaciones del dibujo anatómico */
    @keyframes amygdala-pulse-alert {
      0%, 100% { r: 18px; opacity: 0.95; }
      50% { r: 27px; opacity: 0.45; }
    }
    @keyframes amygdala-pulse-calm {
      0%, 100% { r: 16px; opacity: 0.75; }
      50% { r: 21px; opacity: 0.35; }
    }
    @keyframes eeg-dash-scroll {
      from { stroke-dashoffset: 0; }
      to { stroke-dashoffset: -120; }
    }
    @keyframes vagus-pulse-flow {
      0% { transform: translateY(0); opacity: 1; }
      50% { opacity: 0.8; }
      100% { transform: translateY(16px); opacity: 0.2; }
    }

    .bio-svg-alert .bio-amygdala-glow {
      animation: amygdala-pulse-alert 1.2s infinite ease-in-out;
    }
    .bio-svg-calm .bio-amygdala-glow {
      animation: amygdala-pulse-calm 3.5s infinite ease-in-out;
    }
    .bio-svg-alert .bio-eeg-path {
      animation: eeg-dash-scroll 1.2s linear infinite;
      stroke-dasharray: 200;
    }
    .bio-svg-calm .bio-eeg-path {
      animation: eeg-dash-scroll 4.0s linear infinite;
      stroke-dasharray: 200;
    }
    .bio-vagus-node {
      animation: vagus-pulse-flow 1.5s infinite ease-in-out;
    }
    .bio-vagus-node.v2 { animation-delay: 0.4s; }
    .bio-vagus-node.v3 { animation-delay: 0.8s; }

    /* Pie explicativo del dibujo anatómico */
    .bio-anatomy-footer-box {
      background: var(--bg-surface-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 8px 12px;
      display: flex;
      flex-direction: column;
      gap: 3px;
    }

    .baf-badge {
      font-size: 0.64rem;
      font-weight: 800;
      color: var(--cyan-brand);
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    .baf-text {
      font-size: 0.73rem;
      color: var(--text-body);
      line-height: 1.35;
    }

    .stress-telemetry-visual-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-card);
      padding: 16px 20px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .bio-meters-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 14px;
    }

    .bio-meter-tile {
      background: #F8FAFC;
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .bmt-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 6px;
    }

    .bmt-label {
      font-size: 0.68rem;
      font-weight: 700;
      color: var(--text-body);
    }

    .bmt-val {
      font-size: 0.76rem;
      font-weight: 900;
      font-family: monospace;
      transition: color 0.3s ease;
    }

    .bmt-track {
      width: 100%;
      height: 6px;
      background: rgba(100, 116, 139, 0.12);
      border-radius: 3px;
      overflow: hidden;
    }

    .bmt-bar {
      height: 100%;
      border-radius: 3px;
      transition: width 0.4s ease, background 0.4s ease;
    }
    .bmt-bar.alert {
      background: var(--red-alert);
    }
    .bmt-bar.calm {
      background: var(--emerald-safe);
    }

    .bmt-sub {
      font-size: 0.62rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    /* PROTOCOLO VISUAL EN 3 TARJETAS */
    .visual-protocol-section {
      background: rgba(240, 253, 250, 0.6);
      border: 1px solid rgba(13, 148, 136, 0.2);
      border-radius: 12px;
      padding: 12px 14px;
    }

    .vp-section-title {
      font-size: 0.66rem;
      font-weight: 800;
      color: var(--cyan-brand);
      letter-spacing: 0.05em;
      margin-bottom: 8px;
      text-transform: uppercase;
    }

    .vp-cards-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }

    .vp-card-pill {
      background: #FFFFFF;
      border: 1px solid rgba(13, 148, 136, 0.2);
      border-radius: 10px;
      padding: 8px 10px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .vp-badge {
      font-size: 0.74rem;
      font-weight: 900;
      color: var(--cyan-brand);
      font-family: monospace;
    }

    .vp-pill-title {
      font-size: 0.70rem;
      font-weight: 800;
      color: var(--text-title);
    }

    .vp-pill-desc {
      font-size: 0.62rem;
      color: var(--text-muted);
      line-height: 1.25;
    }

    #stage-cert-full {
      width: 100%;
      max-width: 980px;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .cert-container-card {
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-card);
      padding: 38px 46px;
      box-shadow: var(--shadow-card);
      width: 100%;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 36px;
      align-items: center;
    }

    .cert-input-box {
      margin-bottom: 14px;
    }

    .cert-input-lbl {
      display: block;
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--text-title);
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .cert-input-field {
      width: 100%;
      padding: 11px 16px;
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      font-size: 0.84rem;
      color: var(--text-title);
      outline: none;
      transition: var(--transition);
      font-family: inherit;
    }

    .cert-input-field:focus {
      border-color: var(--cyan-brand);
      box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.12);
    }

    .cert-checkboxes-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 22px;
    }

    .cert-check-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.76rem;
      color: var(--text-body);
      line-height: 1.4;
      cursor: pointer;
    }

    .cert-check-item input[type="checkbox"] {
      margin-top: 2px;
      accent-color: var(--cyan-brand);
    }

    .cert-preview-card {
      background: var(--bg-surface-subtle);
      border: 2px dashed var(--border-subtle);
      border-radius: 14px;
      padding: 24px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    .cert-seal-badge {
      width: 60px;
      height: 60px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 2px solid var(--gold-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 12px;
      box-shadow: 0 4px 12px rgba(217, 119, 6, 0.15);
      color: var(--gold-accent);
      font-size: 0.64rem;
      font-weight: 900;
      text-transform: uppercase;
    }

    /* =========================================================================
       SISTEMA RESPONSIVO MULTIPLATAFORMA
       COMPUTADOR • PANTALLA DIVIDIDA • TELEVISOR (4K) • TABLET • CELULAR
       ========================================================================= */

    /* 1. MODO TELEVISOR Y PANTALLAS GIGANTES / 4K (1921px en adelante) */
    @media (min-width: 1921px) {
      :root {
        font-size: 18px; /* Escala proporcional rem en TV */
      }
      .antigravity-nav-header {
        height: 78px;
        padding: 0 44px;
      }
      .nav-corp-logo {
        height: 36px;
      }
      .nav-program-title {
        font-size: 0.94rem;
      }
      .nav-program-subtitle {
        font-size: 0.78rem;
      }
      .stage-step-pill {
        padding: 8px 18px;
        font-size: 0.78rem;
      }
      .somnibot-copilot-banner {
        top: 86px;
        height: 56px;
        max-width: 1720px;
        padding: 6px 24px;
      }
      .somnibot-banner-text {
        font-size: 0.92rem;
      }
      .main-stages-viewport {
        top: 150px;
        bottom: 74px;
      }
      .antigravity-bottom-dock {
        height: 72px;
        padding: 0 44px;
      }
      .dock-stage-counter {
        font-size: 0.88rem;
      }
      .dock-btn {
        padding: 10px 24px;
        font-size: 0.86rem;
      }
      #stage-brain-full, #stage-breathing-full, #stage-dilemmas-full, #stage-stress-full, #stage-truck-full, #stage-cert-full {
        max-width: 1720px;
      }
      #stage-brain-full {
        grid-template-columns: 440px 1fr;
        gap: 36px;
        max-height: calc(100vh - 250px);
      }
      .hero-h1 {
        font-size: 2.1rem;
      }
    }

    /* 2. LAPTOP Y TABLET HORIZONTAL (hasta 1280px) */
    @media (max-width: 1280px) {
      .antigravity-nav-header {
        padding: 0 16px;
      }
      .stage-step-pill {
        padding: 5px 10px;
        font-size: 0.67rem;
      }
      #stage-brain-full {
        grid-template-columns: 320px 1fr;
        gap: 16px;
      }
      .brain-intro-panel {
        padding: 22px 20px;
      }
      #stage-breathing-full {
        grid-template-columns: 360px 1fr;
        gap: 20px;
      }
      #stage-dilemmas-full {
        grid-template-columns: 380px 1fr;
        gap: 18px;
      }
    }

    /* 3. PANTALLA DIVIDIDA (SPLIT SCREEN) Y TABLET VERTICAL (hasta 1024px) */
    @media (max-width: 1024px) {
      .antigravity-nav-header {
        height: 58px;
        padding: 0 14px;
      }
      .nav-brand-pill {
        gap: 8px;
      }
      .nav-corp-logo {
        height: 22px;
      }
      .nav-program-subtitle {
        display: none; /* Ahorra espacio horizontal en pantalla dividida */
      }
      .nav-program-title {
        font-size: 0.72rem;
      }
      .nav-separator-line {
        height: 18px;
      }

      /* Barra de navegación horizontal desplazable */
      .stages-stepper-row {
        overflow-x: auto;
        white-space: nowrap;
        scrollbar-width: none;
        -webkit-overflow-scrolling: touch;
        padding: 3px 6px;
        gap: 4px;
        max-width: 55%;
      }
      .stages-stepper-row::-webkit-scrollbar {
        display: none;
      }
      .stage-step-pill {
        flex-shrink: 0;
        padding: 4px 8px;
        font-size: 0.64rem;
      }

      /* Banner SomniBot adaptativo */
      .somnibot-copilot-banner {
        top: 64px;
        width: calc(100% - 24px);
        height: auto;
        min-height: 44px;
        padding: 5px 14px;
        gap: 10px;
      }
      .somnibot-banner-text {
        font-size: 0.74rem;
        line-height: 1.35;
      }

      /* Viewport con scroll vertical suave */
      .main-stages-viewport {
        top: 116px;
        bottom: 58px;
        overflow-y: auto;
        overflow-x: hidden;
        -webkit-overflow-scrolling: touch;
      }

      .stage-layer {
        position: relative;
        min-height: 100%;
        height: auto;
        align-items: flex-start;
        justify-content: center;
        padding: 16px 12px 28px 12px;
        overflow-y: visible;
      }
      .stage-layer:not(.is-active) {
        display: none !important;
      }

      /* FASE 0: CEREBRO 3D */
      #stage-brain-full {
        grid-template-columns: 1fr;
        gap: 16px;
        height: auto;
        max-height: none;
      }
      .brain-intro-panel {
        padding: 18px 16px;
      }
      .brain-canvas-container {
        height: 380px;
        min-height: 320px;
        max-height: none;
      }
      .brain-tour-dock {
        flex-wrap: wrap;
        gap: 6px;
        top: 10px; left: 10px; right: 10px;
      }
      .btour-header-group {
        padding: 3px 6px;
        gap: 4px;
      }
      .btour-step-btn {
        padding: 3px 6px;
        font-size: 0.64rem;
      }
      .btour-controls-group {
        padding: 3px 6px;
        gap: 4px;
      }
      .btour-ctrl-btn {
        padding: 3px 8px;
        font-size: 0.64rem;
      }
      .brain-telemetry-dock {
        grid-template-columns: repeat(2, 1fr);
        gap: 8px;
        padding: 8px 12px;
        bottom: 10px; left: 10px; right: 10px;
      }

      /* FASE 1: RESPIRACIÓN 4-7-8 */
      #stage-breathing-full {
        grid-template-columns: 1fr;
        gap: 16px;
        height: auto;
      }
      .breathing-side-panel {
        padding: 20px 18px;
      }
      .resp-phase-giant {
        font-size: 2.2rem;
      }
      .lungs-canvas-container {
        height: 340px;
        min-height: 280px;
      }

      /* FASE 2: SIMULADOR VIAL */
      #stage-truck-full {
        height: 440px;
        min-height: 380px;
      }
      .truck-full-controls-dock {
        bottom: 12px;
        left: 12px;
        right: 12px;
        padding: 6px 14px;
        justify-content: center;
        flex-wrap: wrap;
        gap: 8px;
      }

      /* FASE 3: DECISIONES */
      #stage-dilemmas-full {
        grid-template-columns: 1fr;
        gap: 16px;
        height: auto;
      }
      .dilemma-brain-stage {
        height: 320px;
        min-height: 280px;
      }

      /* FASE 4: FISIOLOGÍA DEL ESTRÉS */
      #stage-stress-full {
        height: auto;
        justify-content: flex-start;
      }
      .stress-header-row {
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
      }
      .stress-quick-toggle-bar {
        width: 100%;
        display: flex;
        gap: 8px;
      }
      .stress-toggle-btn {
        flex: 1;
        text-align: center;
        padding: 7px 10px;
        font-size: 0.72rem;
      }
      .stress-layout-grid {
        grid-template-columns: 1fr;
        gap: 16px;
      }
      .bio-anatomy-svg-wrapper svg {
        max-height: 300px;
      }

      /* FASE 5: CERTIFICADO */
      .cert-container-card {
        grid-template-columns: 1fr;
        gap: 22px;
        padding: 24px 20px;
      }

      /* DOCK INFERIOR */
      .antigravity-bottom-dock {
        height: 56px;
        padding: 0 16px;
      }
      .dock-stage-counter {
        font-size: 0.70rem;
      }
      .dock-btn {
        padding: 7px 14px;
        font-size: 0.74rem;
      }
    }

    /* 4. CELULARES Y SMARTPHONES (hasta 580px) */
    @media (max-width: 580px) {
      .antigravity-nav-header {
        height: 50px;
        padding: 0 8px;
      }
      .nav-brand-pill {
        gap: 5px;
      }
      .nav-corp-logo {
        height: 18px;
      }
      .nav-program-title {
        display: none !important;
      }
      .nav-brand-pill {
        flex-shrink: 0;
        gap: 6px;
      }
      .nav-corp-logo {
        height: 20px;
      }
      .stages-stepper-row {
        flex: 1;
        min-width: 0;
        max-width: none;
      }
      .nav-separator-line {
        height: 14px;
      }
      .stages-stepper-row {
        max-width: 60%;
        gap: 3px;
        padding: 2px 4px;
      }
      .stage-step-pill {
        padding: 3px 6px;
        font-size: 0.58rem;
      }

      .somnibot-copilot-banner {
        top: 54px;
        width: calc(100% - 12px);
        padding: 4px 8px;
        gap: 6px;
        border-radius: 10px;
      }
      .somnibot-banner-avatar-wrap {
        width: 28px;
        height: 28px;
      }
      .somnibot-banner-avatar-img {
        width: 24px;
        height: 24px;
      }
      .somnibot-banner-tag {
        font-size: 0.56rem;
      }
      .somnibot-banner-voice-btn {
        padding: 2px 5px;
        font-size: 0.56rem;
      }
      .somnibot-banner-text {
        font-size: 0.67rem;
        line-height: 1.25;
        max-height: 34px;
        overflow-y: auto;
      }
      .somnibot-eq-bars {
        display: none;
      }

      .main-stages-viewport {
        top: 102px;
        bottom: 50px;
      }
      .stage-layer {
        padding: 8px 6px 18px 6px;
      }

      .hero-h1 {
        font-size: 1.18rem;
        margin-bottom: 6px;
      }
      .hero-desc {
        font-size: 0.76rem;
        line-height: 1.35;
      }
      .intro-pillars-box {
        font-size: 0.72rem;
        padding: 8px 10px;
        line-height: 1.35;
      }
      .intro-actions-row {
        flex-direction: column;
        gap: 6px;
      }
      .hero-cta-btn, .hero-sec-btn {
        width: 100%;
        justify-content: center;
        padding: 9px 14px;
        font-size: 0.74rem;
      }

      .brain-canvas-container {
        height: 290px;
        min-height: 260px;
      }
      .bstep-num {
        display: none;
      }
      .btour-step-btn {
        padding: 3px 5px;
        font-size: 0.60rem;
      }
      .bstep-sep {
        font-size: 0.55rem;
      }
      .telemetry-lbl {
        font-size: 0.52rem;
      }
      .telemetry-val {
        font-size: 0.60rem;
      }

      .lungs-canvas-container {
        height: 280px;
        min-height: 250px;
      }
      .rc-pill {
        font-size: 0.72rem;
        padding: 3px 7px;
      }

      #stage-truck-full {
        height: 330px;
        min-height: 300px;
      }
      .truck-btn-pill {
        padding: 7px 12px;
        font-size: 0.68rem;
      }

      .dilemma-brain-stage {
        height: 260px;
        min-height: 240px;
      }

      .bio-anatomy-svg-wrapper svg {
        max-height: 240px;
      }
      .bio-meters-grid {
        grid-template-columns: 1fr;
      }
      .visual-protocol-section .vp-cards-row {
        grid-template-columns: 1fr;
        gap: 6px;
      }

      .cert-container-card {
        padding: 16px 12px;
      }

      .antigravity-bottom-dock {
        height: 50px;
        padding: 0 10px;
      }
      .dock-stage-counter {
        font-size: 0.60rem;
        max-width: 130px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .dock-btn {
        padding: 6px 10px;
        font-size: 0.68rem;
      }
    }
    </style>
</head>
<body>

  <!-- Lienzo de fondo Antigravity -->
  <canvas id="antigravity-particles-canvas"></canvas>

  <!-- CABECERA INSTITUCIONAL CON LOGOS AUTÉNTICOS -->
  <header class="antigravity-nav-header" role="banner">
    <div class="nav-brand-pill">
      <img src="assets/logo-isaval.png" alt="Logo ISAVAL" class="nav-corp-logo">
      <div class="nav-separator-line"></div>
      <div>
        <div class="nav-program-title">PROGRAMA SG-SST • HIGIENE DEL SUEÑO</div>
        <div class="nav-program-subtitle">Prevención de Fatiga, Microsueños y Descompresión Neurobiológica</div>
      </div>
    </div>

    <nav class="stages-stepper-row" role="tablist">
      <button type="button" class="stage-step-pill is-active" data-stage="0">
        <span class="pill-full">01. CEREBRO 3D INTERACTIVO</span>
        <span class="pill-short">01. CEREBRO</span>
      </button>
      <button type="button" class="stage-step-pill" data-stage="1">
        <span class="pill-full">02. RESPIRACIÓN 4-7-8</span>
        <span class="pill-short">02. RESPIRACIÓN</span>
      </button>
      <button type="button" class="stage-step-pill" data-stage="2">
        <span class="pill-full">03. SIMULADOR VIAL POV</span>
        <span class="pill-short">03. SIMULADOR</span>
      </button>
      <button type="button" class="stage-step-pill" data-stage="3">
        <span class="pill-full">04. DECISIONES DE TURNO</span>
        <span class="pill-short">04. DECISIONES</span>
      </button>
      <button type="button" class="stage-step-pill" data-stage="4">
        <span class="pill-full">05. FISIOLOGÍA DEL ESTRÉS</span>
        <span class="pill-short">05. ESTRÉS</span>
      </button>
      </nav>
  </header>

  <!-- BANNER COPILOTO ASISTENTE SOMNIBOT SG-SST (100% LIBRE DE SUPERPOSICIÓN DE TEXTO) -->
  <aside class="somnibot-copilot-banner" aria-label="Asistente SomniBot SG-SST">
    <div class="somnibot-banner-avatar-wrap" id="somnibot-trigger" title="Haz clic para repetir la narración de voz">
      <div class="somnibot-pulse-ring"></div>
      <img src="assets/bot_cerebrito.png" alt="Cerebrito SST" class="somnibot-banner-avatar-img">
    </div>
    <div class="somnibot-banner-body">
      <div class="somnibot-banner-tagline">
        <span class="somnibot-banner-tag">SOMNIBOT • GUÍA SG-SST</span>
        <button type="button" class="somnibot-banner-voice-btn" id="btn-toggle-voice">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
          <span id="label-voice-status">Voz Activada</span>
        </button>
      </div>
      <div class="somnibot-banner-text" id="somnibot-text-target">
        Bienvenido al programa de higiene del sueño de ISAVAL SG-SST. Explora cada módulo interactivo para potenciar tu seguridad vial y laboral.
      </div>
    </div>
    <div class="somnibot-banner-right">
      <div class="somnibot-eq-bars" id="somnibot-eq-indicator" title="Audio activo">
        <div class="somnibot-eq-bar"></div>
        <div class="somnibot-eq-bar"></div>
        <div class="somnibot-eq-bar"></div>
        <div class="somnibot-eq-bar"></div>
      </div>
    </div>
  </aside>

  <!-- CONTENEDOR PRINCIPAL DE FASES -->
  <main class="main-stages-viewport" role="main">

    <!-- FASE 1: CEREBRO ANATÓMICO 3D INTERACTIVO (ROTAR Y MIRAR POR DENTRO) -->
    <section class="stage-layer is-active" id="stage-0" aria-label="Cerebro 3D Interactivo">
      <div id="stage-brain-full">
        <div class="brain-intro-panel">
          <div class="hero-eyebrow">PROGRAMA SG-SST • SALUD Y SEGURIDAD LABORAL</div>
          <h1 class="hero-h1">Higiene del Sueño y Alerta Operativa</h1>
          <p class="hero-desc">
            El descanso es un proceso biológico activo: durante el sueño profundo, tu cerebro drena toxinas celulares, consolida la memoria y restablece la velocidad de tus reflejos para una conducción y trabajo seguros.
          </p>

          <div class="intro-pillars-box">
            <strong>Factores clave de seguridad en ruta:</strong><br>
            • <strong>Reflejos y respuesta:</strong> Dormir menos de 6 horas deteriora tu velocidad de frenado de forma idéntica a una intoxicación etílica.<br>
            • <strong>Prevención de microsueños:</strong> 3 segundos de cabeceo a 80 km/h representan 67 metros de desplazamiento completamente a ciegas.<br>
            • <strong>Descompresión preventiva:</strong> Desactivar el estrés antes de dormir asegura un sueño continuo y una jornada libre de accidentes.
          </div>

          <div class="intro-actions-row">
            <button type="button" class="hero-cta-btn" id="btn-start-exp-breath" onclick="goToStage(1)">
              <span style="white-space:nowrap;">Técnica 4-7-8 →</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            </button>
            <button type="button" class="hero-sec-btn" id="btn-hero-tour-toggle" onclick="toggleBrainTourPlayPause()">
              <span id="label-hero-tour-toggle">Pausar Ruta Guiada</span>
            </button>
          </div>
        </div>

        <div class="brain-canvas-container" id="brain-container-box" title="Arrastra con el mouse para rotar en 3D. Usa la rueda para acercar o alejar.">
          <canvas id="anatomical-brain-canvas"></canvas>

          <!-- Barra superior de controles 3D -->
          <!-- Barra superior de la RUTA GUIADA del cerebro 3D - DISEÑO COMPACTO Y NUNCA CORTADO -->
          <div class="brain-tour-dock" id="brain-tour-dock">
            <div class="btour-header-group">
              <span class="btour-badge">RUTA NEURAL</span>
              <div class="btour-steps-stepper">
                <button type="button" class="btour-step-btn is-active" id="btour-step-1" onclick="setBrainTourStep(1, true)" title="Paso 1: Sueño Delta Reparador">
                  <span class="bstep-num">1</span>
                  <span>Delta</span>
                </button>
                <span class="bstep-sep">→</span>
                <button type="button" class="btour-step-btn" id="btour-step-2" onclick="setBrainTourStep(2, true)" title="Paso 2: Estructuras Límbicas en Reposo">
                  <span class="bstep-num">2</span>
                  <span>Límbico</span>
                </button>
                <span class="bstep-sep">→</span>
                <button type="button" class="btour-step-btn" id="btour-step-3" onclick="setBrainTourStep(3, true)" title="Paso 3: Sobrecarga por Estrés">
                  <span class="bstep-num">3</span>
                  <span>Estrés</span>
                </button>
                <span class="bstep-sep">→</span>
                <button type="button" class="btour-step-btn" id="btour-step-4" onclick="setBrainTourStep(4, true)" title="Paso 4: Fatiga Cortical y Adenosina">
                  <span class="bstep-num">4</span>
                  <span>Fatiga</span>
                </button>
              </div>
            </div>

            <div class="btour-controls-group">
              <button type="button" class="btour-ctrl-btn" id="btn-tour-prev" onclick="brainTourPrev()" title="Paso anterior">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
                <span>Ant</span>
              </button>
              <button type="button" class="btour-ctrl-btn is-play-pause" id="btn-tour-play-pause" onclick="toggleBrainTourPlayPause()" title="Pausar o reanudar ruta">
                <span id="icon-tour-play-pause" style="display:inline-flex; align-items:center;">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>
                </span>
                <span id="label-tour-play-pause">Pausar</span>
              </button>
              <button type="button" class="btour-ctrl-btn" id="btn-tour-next" onclick="brainTourNext()" title="Siguiente paso">
                <span>Sig</span>
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
              </button>
              <button type="button" class="btour-ctrl-btn" id="btn-tour-restart" onclick="restartBrainTour()" title="Reiniciar recorrido">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg>
              </button>
            </div>
          </div>

          <!-- Telemetría médica inferior -->
          <div class="brain-telemetry-dock">
            <div class="telemetry-item">
              <span class="telemetry-lbl">Estado Biológico</span>
              <span class="telemetry-val" id="b-state" style="color: var(--cyan-brand);">ONDAS DELTA (REPARACIÓN)</span>
            </div>
            <div class="telemetry-item">
              <span class="telemetry-lbl">Frecuencia EEG</span>
              <span class="telemetry-val" id="b-freq">2.1 Hz</span>
            </div>
            <div class="telemetry-item">
              <span class="telemetry-lbl">Sistema Dominante</span>
              <span class="telemetry-val" id="b-sys">LAVADO GLINFÁTICO ACTIVO</span>
            </div>
            <div class="telemetry-item">
              <span class="telemetry-lbl">Melatonina</span>
              <span class="telemetry-val" id="b-mel" style="color: var(--gold-accent);">ALTA (92 pg/mL)</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 2: BIOMECÁNICA PULMONAR 4-7-8 CON DETENCIÓN TOTAL (APNEA 7s) -->
    <section class="stage-layer" id="stage-1" aria-label="Descompresión Respiratoria 4-7-8">
      <div id="stage-breathing-full">
        <div class="breathing-side-panel">
          <div class="resp-badge-top" id="resp-badge-tag">DESCOMPRESIÓN NEURAL • MÉTODO 4-7-8</div>
          <div class="resp-phase-giant" id="breath-phase-title">Técnica Diafragmática</div>
          <div class="resp-counter-giant" id="breath-num-countdown">
            <div class="resp-cycle-pills-row">
              <span class="rc-pill">Inhala 4s</span>
              <span class="rc-arrow">→</span>
              <span class="rc-pill">Retén 7s</span>
              <span class="rc-arrow">→</span>
              <span class="rc-pill">Exhala 8s</span>
            </div>
          </div>
          <div class="resp-instructions-text" id="breath-inst-text">
            Esta técnica estimula directamente el nervio vago mediante respiración diafragmática. La retención y exhalación prolongadas desaceleran el pulso cardíaco, reducen el cortisol y facilitan la entrada al sueño profundo Delta.
          </div>

          <div class="resp-mechanics-card">
            <div class="resp-mechanics-title">EFECTO NEUROBIOLÓGICO COMPROBADO</div>
            <div class="resp-mechanics-desc" id="resp-mechanics-detail">
              Desactiva la hiperalerta del turno laboral y prepara el organismo para un descanso continuo y reparador.
            </div>
          </div>

          <div class="resp-control-buttons-row">
            <button type="button" class="hero-cta-btn" id="btn-toggle-breath-play">
              <span id="label-toggle-breath">Comenzar Ejercicio Guiado</span>
            </button>
            <button type="button" class="hero-sec-btn" id="btn-next-to-truck">
              <span>Siguiente: Simulador Vial</span>
            </button>
          </div>
        </div>

        <div class="breathing-canvas-container">
          <div class="breath-hud-hold-pill" id="breath-hold-pill">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>
            <span>APNEA ACTIVA • DETENCIÓN TOTAL DEL FLUJO (7 SEG)</span>
          </div>
          <canvas id="breath-rings-canvas"></canvas>
        </div>
      </div>
    </section>

    <!-- FASE 3: SIMULADOR VIAL POV PROCEDURAL Y REALISTA (ANIMACIÓN ACTIVA) -->
    <section class="stage-layer" id="stage-2" aria-label="Simulador de Conducción Vial Realista">
      <div id="stage-truck-full">
        <canvas id="truck-full-canvas"></canvas>

        <div class="eyelid-full-top" id="truck-eyelid-top"></div>
        <div class="eyelid-full-bottom" id="truck-eyelid-bottom"></div>

        <div class="truck-full-blackout" id="truck-blackout-full">
          <div style="font-size: 1.8rem; font-weight: 900; color: #ef4444; margin-bottom: 12px; letter-spacing: 0.05em;">
            MICROSUEÑO EN CURSO: 3 SEGUNDOS DE DESCONEXIÓN TOTAL
          </div>
          <p style="font-size: 0.94rem; max-width: 580px; color: #e2e8f0; line-height: 1.6;">
            Tus ojos se cerraron involuntariamente. A 80 km/h, tu vehículo avanza 22.2 metros por cada segundo. En este instante estás cruzando más de 66 metros completamente a ciegas...
          </p>
        </div>

        <div class="truck-full-crash" id="truck-crash-full">
          <div style="font-size: 2.2rem; font-weight: 900; margin-bottom: 8px; letter-spacing: 0.04em;">
            IMPACTO VIAL POR MICROSUEÑO
          </div>
          <div style="font-size: 1.1rem; font-weight: 800; color: #fef08a; margin-bottom: 16px;">
            INFORME DE ANÁLISIS DE CAUSA RAÍZ SG-SST
          </div>
          <div style="background: rgba(0,0,0,0.65); border: 1px solid rgba(255,255,255,0.25); border-radius: 12px; padding: 18px 24px; max-width: 680px; text-align: left; font-size: 0.84rem; line-height: 1.6; margin-bottom: 24px;">
            <strong>Mecanismo Biológico del Accidente:</strong> La deuda de sueño acumulada satura los receptores de adenosina en el tronco encefálico. El cerebro fuerza micro-desconexiones corticales para inducir sueño de onda lenta sin previo aviso.<br><br>
            <strong>Protocolo de Prevención ISAVAL SG-SST:</strong><br>
            • Dormir un mínimo de 7 horas continuas antes de tomar turno de conducción.<br>
            • Si experimentas bostezo continuo o pesadez en párpados, detén el vehículo en un lugar seguro y realiza una pausa activa de 15 minutos.<br>
            • Jamás intentes compensar el sueño únicamente con cafeína, bebidas energizantes o ventilación fría.
          </div>
          <div id="truck-auto-next-tag" style="font-size: 0.95rem; font-weight: 700; color: #fef08a; margin-top: 10px; margin-bottom: 12px; letter-spacing: 0.02em;">Avanzando a Decisiones de Turno en 8s...</div>
          <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
            <button type="button" class="hero-cta-btn" id="btn-restart-driving-full" style="background: #FFFFFF; color: #b91c1c;">
              <span>Reiniciar Simulador</span>
            </button>
            <button type="button" class="hero-cta-btn" id="btn-crash-to-dilemmas" onclick="goToStage(3)" style="background: var(--cyan-brand); color: #FFFFFF; box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4);">
              <span>Continuar a Decisiones de Turno &rarr;</span>
            </button>
          </div>
        </div>

        <div class="truck-full-controls-dock">
          <button type="button" class="truck-btn-pill" id="btn-steer-left-full">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
            <span>Girar Izq</span>
          </button>
          <button type="button" class="truck-btn-pill" id="btn-steer-right-full">
            <span>Girar Der</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
          </button>
          <button type="button" class="truck-btn-pill" id="btn-drive-accel-full">
            <span id="label-accel-full">Frenar / Detener</span>
          </button>
          <button type="button" class="truck-btn-pill danger" id="btn-trigger-microsleep-full">
            <span>Simular Microsueño</span>
          </button>

          <div class="truck-fatigue-hud-pill">
            <span>SOMNOLENCIA:</span>
            <span id="truck-fatigue-pct-full" style="color:var(--emerald-safe);">0% (ALERTA)</span>
            <div class="tf-track">
              <div class="tf-fill" id="truck-fatigue-fill-full"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 4: DECISIONES DE TURNO -->
    <section class="stage-layer" id="stage-3" aria-label="Decisiones de Turno">
      <div id="stage-dilemmas-full">
        <div class="dilemma-brain-stage">
          <div class="dil-brain-top-tag">MONITOR NEURAL EN TIEMPO REAL • REACCIÓN COGNITIVA</div>
          <canvas id="dilemma-brain-canvas"></canvas>
          <div class="dil-brain-bottom-telemetry">
            <div>ESTADO: <span id="dil-telemetry-state" style="color:var(--cyan-brand);">EQUILIBRIO (CALMA)</span></div>
            <div>FRECUENCIA: <span id="dil-telemetry-freq" style="color:var(--text-title);">10.2 Hz (ALFA)</span></div>
          </div>
        </div>

        <div class="dilemma-content-card">
          <div class="dilemma-step-header" id="dil-category-tag">DECISIÓN 01 • DESCANSO PREVIO AL TURNO</div>
          <h2 class="dilemma-title-h2" id="dil-question-text">¿Qué haces 45 minutos antes de dormir?</h2>
          <p class="dilemma-desc-p" id="dil-context-text">
            La exposición a luz azul de pantallas inhibe la liberación de melatonina y engaña al cerebro haciéndole creer que es mediodía.
          </p>

          <div class="dilemma-choices-container">
            <button type="button" class="neutral-choice-card" id="btn-dil-a">
              <span class="choice-tag">OPCIÓN A</span>
              <span class="choice-body-text" id="text-dil-opt-a">Revisar celular en la cama con brillo alto</span>
            </button>
            <button type="button" class="neutral-choice-card" id="btn-dil-b">
              <span class="choice-tag">OPCIÓN B</span>
              <span class="choice-body-text" id="text-dil-opt-b">Desconexión digital con luz tenue y respiración 4-7-8</span>
            </button>
          </div>

          <div class="dilemma-explanation-box" id="dil-explanation-box"></div>

          <div style="margin-top: 20px; display: flex; justify-content: flex-end;">
            <button type="button" class="hero-cta-btn" id="btn-dil-next-scenario" style="display: none;">
              <span>Siguiente Decisión</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 5: IMPACTO DE HÁBITOS • COMPARATIVA BIOMÉDICA EJECUTIVA (SIN DIBUJOS ANIMADOS) -->
    <section class="stage-layer" id="stage-4" aria-label="Fisiología del Estrés y el Cerebro">
      <div id="stage-stress-full">
        <!-- Cabecera del Módulo -->
        <div class="stress-header-row">
          <div>
            <div class="hero-eyebrow">PROGRAMA SG-SST • BIOCIRCUITO DEL ESTRÉS Y EL SUEÑO</div>
            <h2 style="font-size: 1.55rem; font-weight: 900; color: var(--text-title); letter-spacing: -0.02em;">
              Fisiología del Estrés y Recuperación Cerebral
            </h2>
            <p style="font-size: 0.82rem; color: var(--text-muted); margin-top: 2px;">
              Diagrama interactivo del circuito biológico: compara el impacto de la sobrecarga operativa frente a la descompresión vagal.
            </p>
          </div>
          <div class="stress-quick-toggle-bar">
            <button type="button" class="stress-toggle-btn is-active" id="btn-stress-mode-alert">
              Sobrecarga por Estrés (Alerta Simpática)
            </button>
            <button type="button" class="stress-toggle-btn" id="btn-stress-mode-calm">
              Descompresión y Reparación (Tono Vagal)
            </button>
          </div>
        </div>

        <!-- Cuadrícula Gráfica: Biocircuito + Monitor Biométrico -->
        <div class="stress-layout-grid">
          
          <!-- COLUMNA 1: DIBUJO ANATÓMICO Y BIOCIRCUITO DEL EJE ESTRÉS-SUEÑO -->
          <div class="stress-anatomy-art-card">
            <div class="bio-circuit-badge-bar">
              <span class="bio-circuit-badge" id="bio-circuit-mode-title">DIBUJO ANATÓMICO • EJE CEREBRO-ESTRÉS-CONDUCCIÓN</span>
              <span class="bio-status-pill alert" id="bio-circuit-status-pill">Sobrecarga Activa</span>
            </div>

            <!-- SVG Anatómico Vectorial de Alta Resolución Médica -->
            <div class="bio-anatomy-svg-wrapper">
              <svg id="bio-anatomy-svg" viewBox="0 0 620 370" class="bio-svg-alert" xmlns="http://www.w3.org/2000/svg">
                <defs>
                  <filter id="glow-alert" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="3" result="blur"/>
                    <feMerge>
                      <feMergeNode in="blur"/>
                      <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                  </filter>
                  <filter id="glow-calm" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="3" result="blur"/>
                    <feMerge>
                      <feMergeNode in="blur"/>
                      <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                  </filter>
                  <radialGradient id="grad-amygdala-alert" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" stop-color="#ff1a40" stop-opacity="0.95"/>
                    <stop offset="50%" stop-color="#dc2626" stop-opacity="0.75"/>
                    <stop offset="100%" stop-color="#991b1b" stop-opacity="0"/>
                  </radialGradient>
                  <radialGradient id="grad-amygdala-calm" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.95"/>
                    <stop offset="50%" stop-color="#0284c7" stop-opacity="0.70"/>
                    <stop offset="100%" stop-color="#075985" stop-opacity="0"/>
                  </radialGradient>
                  <radialGradient id="grad-cortex-fill" cx="48%" cy="42%" r="56%">
                    <stop offset="0%" stop-color="#ffffff" stop-opacity="0.9"/>
                    <stop offset="55%" stop-color="#f8fafc" stop-opacity="0.8"/>
                    <stop offset="100%" stop-color="#e2e8f0" stop-opacity="0.5"/>
                  </radialGradient>
                </defs>

                <!-- Fondo y rejilla sutil biomédica -->
                <rect x="0" y="0" width="620" height="370" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
                <g stroke="#E2E8F0" stroke-width="0.6" stroke-dasharray="3,3" opacity="0.6">
                  <line x1="150" y1="0" x2="150" y2="370" />
                  <line x1="470" y1="0" x2="470" y2="370" />
                  <line x1="0" y1="120" x2="620" y2="120" />
                  <line x1="0" y1="240" x2="620" y2="240" />
                </g>

                <!-- ========================================================
                     ZONA CENTRAL ANATÓMICA (100% DESPEJADA, CENTRADA Y SIN BLOQUEOS)
                     Silueta visible entre X=190 y X=433. Cuadros en X<=172 y X>=448.
                     ======================================================== -->
                <g id="bio-anatomy-central" transform="translate(98, 14) scale(0.77)">
                  <!-- 1. SILUETA HUMANA DE PERFIL (CRÁNEO, ROSTRO Y CUELLO) -->
                  <path class="bio-silhouette-path" d="M 215,368 L 215,295 C 215,268 208,245 190,225 C 182,216 172,208 165,198 C 156,186 150,172 147,156 C 145,142 147,130 143,122 C 138,114 126,110 120,102 C 114,94 115,84 121,76 C 127,68 136,66 142,62 C 152,42 172,22 202,12 C 235,2 278,-1 318,8 C 362,18 402,46 422,90 C 435,120 435,158 420,192 C 405,225 376,252 352,270 C 335,282 325,298 325,325 L 325,368 Z" 
                        fill="rgba(241, 245, 249, 0.75)" stroke="#CBD5E1" stroke-width="1.8" />

                  <!-- 2. SUSTANCIA CEREBRAL SAGITAL (ENCÉFALO) -->
                  <path class="bio-brain-mass" d="M 188,142 C 176,122 180,88 200,66 C 226,38 270,32 304,36 C 342,40 380,62 396,98 C 408,124 404,158 386,182 C 372,202 346,215 324,220 C 302,225 285,214 268,204 C 252,210 236,212 220,204 C 200,192 192,165 188,142 Z" 
                        fill="url(#grad-cortex-fill)" stroke="#94A3B8" stroke-width="1.8" />

                  <!-- GIROS Y SURCOS CEREBRALES (SULCI) -->
                  <g class="bio-sulci-paths" fill="none" stroke="#94A3B8" stroke-width="1.4" stroke-linecap="round" opacity="0.85">
                    <path d="M 210,95 Q 235,78 265,88 T 315,78 T 355,95" />
                    <path d="M 225,122 Q 255,108 288,118 T 345,110 T 378,128" />
                    <path d="M 240,150 Q 272,136 310,144 T 362,142" />
                    <path d="M 265,178 Q 298,170 338,175" />
                  </g>

                  <!-- CEREBELO POSTERIOR -->
                  <path class="bio-cerebellum-mass" d="M 340,195 C 368,200 384,222 374,244 C 360,260 334,258 312,248 C 302,242 296,230 302,214 Z" 
                        fill="#E2E8F0" stroke="#94A3B8" stroke-width="1.6" />
                  <g fill="none" stroke="#64748B" stroke-width="1" opacity="0.6">
                    <path d="M 320,225 Q 345,220 365,230" />
                    <path d="M 326,238 Q 348,232 360,242" />
                  </g>

                  <!-- TRONCO ENCEFÁLICO -->
                  <path class="bio-brainstem-path" d="M 284,202 C 282,235 278,275 274,330 L 260,330 C 264,275 268,235 270,202 Z" 
                        fill="#CBD5E1" stroke="#94A3B8" stroke-width="1.6" />

                  <!-- 3. SISTEMA LÍMBICO: AMÍGDALA & HIPOCAMPO -->
                  <path class="bio-hippocampus-path" d="M 252,176 C 240,164 244,148 258,142 C 275,135 294,146 296,164 C 298,178 285,188 270,185" 
                        fill="none" stroke="#64748B" stroke-width="2.5" stroke-linecap="round" />
                  <circle id="bio-amygdala-glow" class="bio-amygdala-glow" cx="248" cy="168" r="22" fill="url(#grad-amygdala-alert)" />
                  <circle id="bio-amygdala-core" class="bio-amygdala-core" cx="248" cy="168" r="9" fill="#DC2626" stroke="#FFFFFF" stroke-width="2" />
                  <g id="bio-amygdala-bursts" class="bio-amygdala-bursts" stroke="#EF4444" stroke-width="1.6" stroke-linecap="round">
                    <line x1="248" y1="168" x2="228" y2="152" />
                    <line x1="248" y1="168" x2="222" y2="176" />
                    <line x1="248" y1="168" x2="238" y2="192" />
                    <line x1="248" y1="168" x2="265" y2="188" />
                  </g>

                  <!-- 4. EJE NERVIO VAGO Y VÍAS DESCENDENTES (EN EL CUELLO / MÉDULA) -->
                  <g class="bio-vagus-nerve-group">
                    <path id="bio-vagus-fiber" class="bio-vagus-fiber alert" d="M 270,210 C 268,245 262,280 258,340" 
                          fill="none" stroke="#EF4444" stroke-width="2.5" stroke-dasharray="4,3" />
                    <circle class="bio-vagus-node v1 alert" cx="268" cy="240" r="3.5" fill="#DC2626" />
                    <circle class="bio-vagus-node v2 alert" cx="264" cy="275" r="3.5" fill="#DC2626" />
                    <circle class="bio-vagus-node v3 alert" cx="260" cy="310" r="3.5" fill="#DC2626" />
                  </g>

                  <!-- 5. PINES / HOTSPOTS INTERACTIVOS CLÍNICOS -->
                  <g class="bio-hotspot-pin" id="pin-amygdala" onclick="selectBioHotspot('amygdala')" transform="translate(248, 168)" style="cursor:pointer;">
                    <circle cx="0" cy="0" r="13" fill="none" stroke="#DC2626" stroke-width="1.5" opacity="0.75" class="pin-ring" />
                    <circle cx="0" cy="0" r="4.5" fill="#DC2626" />
                    <rect x="12" y="-10" width="76" height="20" rx="5" fill="#0F172A" opacity="0.9" />
                    <text x="18" y="4" font-size="8.8" font-weight="800" fill="#FFFFFF">1. Amígdala</text>
                  </g>

                  <g class="bio-hotspot-pin" id="pin-vagus" onclick="selectBioHotspot('vagus')" transform="translate(262, 275)" style="cursor:pointer;">
                    <circle cx="0" cy="0" r="13" fill="none" stroke="#DC2626" stroke-width="1.5" opacity="0.75" class="pin-ring" />
                    <circle cx="0" cy="0" r="4.5" fill="#DC2626" />
                    <rect x="12" y="-10" width="86" height="20" rx="5" fill="#0F172A" opacity="0.9" />
                    <text x="18" y="4" font-size="8.8" font-weight="800" fill="#FFFFFF">2. Nervio Vago</text>
                  </g>
                </g>

                <!-- LÍNEAS GUÍA (LEADER LINES) SUTILES SIN INTERFERENCIA -->
                <g stroke="#CBD5E1" stroke-width="1.1" stroke-dasharray="3,3" fill="none">
                  <path d="M 186,58 L 210,58 L 230,95" />
                  <path d="M 186,156 L 215,156 L 255,158" />
                  <path d="M 434,58 L 410,58 L 385,76" />
                  <path d="M 434,164 L 390,164 L 340,250" />
                </g>
                <circle id="lead-dot-1" cx="230" cy="95" r="3" fill="#DC2626" opacity="0.85" />
                <circle id="lead-dot-2" cx="255" cy="158" r="3" fill="#DC2626" opacity="0.85" />
                <circle id="lead-dot-3" cx="385" cy="76" r="3" fill="#DC2626" opacity="0.85" />
                <circle id="lead-dot-4" cx="340" cy="250" r="3" fill="#DC2626" opacity="0.85" />

                <!-- ========================================================
                     COLUMNA LATERAL IZQUIERDA: ALINEACIÓN Y LEGIBILIDAD (X=10, W=176)
                     ======================================================== -->
                <!-- 1. DEPURACIÓN GLINFÁTICA -->
                <g class="bio-widget-box" transform="translate(10, 16)">
                  <rect x="0" y="0" width="176" height="88" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2" filter="drop-shadow(0 3px 8px rgba(0,0,0,0.05))" />
                  <circle cx="21" cy="20" r="9" fill="rgba(239, 68, 68, 0.1)" id="bio-glymph-icon-bg" />
                  <path id="bio-glymph-icon-path" d="M 21,14 C 21,14 17,19 17,22 A 4,4 0 0,0 25,22 C 25,19 21,14 21,14 Z" fill="#DC2626" />
                  <text x="35" y="23" font-size="9.0" font-weight="900" fill="#475569" letter-spacing="0.3">DEPURACIÓN GLINFÁTICA</text>
                  
                  <text x="14" y="48" id="bio-glymph-val" font-size="14.5" font-weight="900" fill="#DC2626">0% DRENAJE</text>
                  
                  <!-- Barra de progreso biomédica -->
                  <rect x="14" y="55" width="148" height="4" rx="2" fill="#F1F5F9" />
                  <rect id="bio-glymph-bar" x="14" y="55" width="8" height="4" rx="2" fill="#DC2626" />
                  
                  <text x="14" y="74" id="bio-glymph-sub" font-size="8.4" font-weight="700" fill="#64748B">Adenosina estancada en corteza</text>
                </g>

                <!-- 2. EJE SUPRARRENAL & HORMONAS -->
                <g class="bio-widget-box" transform="translate(10, 116)">
                  <rect x="0" y="0" width="176" height="88" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2" filter="drop-shadow(0 3px 8px rgba(0,0,0,0.05))" />
                  <circle cx="21" cy="20" r="9" fill="rgba(239, 68, 68, 0.1)" id="bio-hormone-icon-bg" />
                  <path id="bio-hormone-icon-path" d="M 21,14 L 21,26 M 17,17 L 25,23 M 17,23 L 25,17" stroke="#DC2626" stroke-width="1.8" stroke-linecap="round" />
                  <text x="35" y="23" font-size="9.0" font-weight="900" fill="#475569" letter-spacing="0.3">EJE SUPRARRENAL</text>
                  
                  <text x="14" y="48" id="bio-hormone-val" font-size="11.4" font-weight="900" fill="#DC2626">Cortisol: +180% Sérico</text>
                  
                  <!-- Barra de cortisol -->
                  <rect x="14" y="55" width="148" height="4" rx="2" fill="#F1F5F9" />
                  <rect id="bio-hormone-bar" x="14" y="55" width="140" height="4" rx="2" fill="#DC2626" />
                  
                  <text x="14" y="74" id="bio-hormone-sub" font-size="8.4" font-weight="700" fill="#64748B">Melatonina bloqueada</text>
                </g>

                <!-- ========================================================
                     COLUMNA LATERAL DERECHA: ALINEACIÓN Y LEGIBILIDAD (X=434, W=176)
                     ======================================================== -->
                <!-- 3. MONITOR ONDAS EEG EN VIVO -->
                <g class="bio-eeg-monitor" transform="translate(434, 16)">
                  <rect x="0" y="0" width="176" height="88" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2" filter="drop-shadow(0 3px 8px rgba(0,0,0,0.05))" />
                  <text x="14" y="23" font-size="9.0" font-weight="900" fill="#475569" letter-spacing="0.3">MONITOR ONDAS EEG</text>
                  <rect x="14" y="28" width="148" height="30" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="0.8" />
                  <line x1="14" y1="43" x2="162" y2="43" stroke="#E2E8F0" stroke-width="0.6" stroke-dasharray="2,2" />
                  <path id="bio-eeg-path" class="bio-eeg-path alert" d="M 18,43 L 28,43 L 33,35 L 40,49 L 47,36 L 55,48 L 63,43 L 75,43 L 82,34 L 90,50 L 98,36 L 106,48 L 114,43 L 126,43 L 133,35 L 145,43" 
                        fill="none" stroke="#DC2626" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
                  <text x="14" y="74" id="bio-eeg-text" font-size="8.4" font-weight="800" fill="#DC2626">BETA 28.4 Hz • HIPERALERTA</text>
                </g>

                <!-- 4. RIESGO EN CONDUCCIÓN & TAQUÍMETRO DE VIALIDAD -->
                <g class="bio-widget-box" transform="translate(434, 116)">
                  <rect x="0" y="0" width="176" height="120" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2" filter="drop-shadow(0 3px 8px rgba(0,0,0,0.05))" />
                  <text x="14" y="23" font-size="9.0" font-weight="900" fill="#475569" letter-spacing="0.3">RIESGO EN CONDUCCIÓN</text>
                  
                  <!-- Indicador de aguja -->
                  <path d="M 20,58 A 16,16 0 1,1 52,58" fill="none" stroke="#E2E8F0" stroke-width="3.5" stroke-linecap="round" />
                  <path id="bio-dial-arc" d="M 20,58 A 16,16 0 1,1 52,58" fill="none" stroke="#DC2626" stroke-width="3.5" stroke-linecap="round" />
                  <line id="bio-dial-needle" x1="36" y1="55" x2="48" y2="43" stroke="#DC2626" stroke-width="2.2" stroke-linecap="round" />
                  <circle cx="36" cy="55" r="3" fill="#0F172A" />

                  <text x="62" y="49" id="bio-drive-risk-val" font-size="17" font-weight="900" fill="#DC2626">15.0x</text>
                  <text x="62" y="62" id="bio-drive-risk-lbl" font-size="8.4" font-weight="800" fill="#64748B">Riesgo Microsueño</text>
                  
                  <rect x="14" y="76" width="148" height="32" rx="6" fill="rgba(239, 68, 68, 0.08)" id="bio-drive-desc-bg" />
                  <text x="18" y="96" id="bio-drive-desc-txt" font-size="8.2" font-weight="800" fill="#DC2626">Cabeceo 3 a 5s = 67m a ciegas</text>
                </g>
              </svg>
            </div>

            <!-- Pie explicativo del dibujo anatómico -->
            <div class="bio-anatomy-footer-box" id="bio-anatomy-footer">
              <div class="baf-badge" id="baf-organ-tag">CORTE SAGITAL • HIPERACTIVACIÓN AMIGDALINA</div>
              <div class="baf-text" id="baf-organ-desc">
                La sobrecarga operativa activa la amígdala cerebral, inhibiendo el freno consciente de la corteza prefrontal, disparando el cortisol y bloqueando el lavado glinfático nocturno.
              </div>
            </div>
          </div>

          <!-- COLUMNA 2: TABLERO BIOMÉTRICO VISUAL Y PROTOCOLO EN 3 TARJETAS -->
          <div class="stress-telemetry-visual-card">
            <div class="scard-header-badge alert" id="scard-telemetry-badge">
              MONITOR BIOMÉDICO • COLAPSO POR ESTRÉS
            </div>

            <!-- Medidores Gráficos -->
            <div class="bio-meters-grid">
              
              <div class="bio-meter-tile">
                <div class="bmt-header">
                  <span class="bmt-label">Cortisol Sérico</span>
                  <span class="bmt-val" id="bm-val-cortisol">28.6 µg/dL</span>
                </div>
                <div class="bmt-track"><div class="bmt-bar alert" id="bm-bar-cortisol" style="width: 92%;"></div></div>
                <div class="bmt-sub" id="bm-sub-cortisol">Nivel Crítico • Toxicidad Suprarrenal</div>
              </div>

              <div class="bio-meter-tile">
                <div class="bmt-header">
                  <span class="bmt-label">Variabilidad Cardíaca (HRV)</span>
                  <span class="bmt-val" id="bm-val-hrv">21 ms</span>
                </div>
                <div class="bmt-track"><div class="bmt-bar alert" id="bm-bar-hrv" style="width: 25%;"></div></div>
                <div class="bmt-sub" id="bm-sub-hrv">Colapso Autónomo • Tono Vagal Mínimo</div>
              </div>

              <div class="bio-meter-tile">
                <div class="bmt-header">
                  <span class="bmt-label">Lavado Glinfático</span>
                  <span class="bmt-val" id="bm-val-glinf">0% BLOQUEADO</span>
                </div>
                <div class="bmt-track"><div class="bmt-bar alert" id="bm-bar-glinf" style="width: 4%;"></div></div>
                <div class="bmt-sub" id="bm-sub-glinf">Adenosina Estancada • Toxicidad Celular</div>
              </div>

              <div class="bio-meter-tile">
                <div class="bmt-header">
                  <span class="bmt-label">Riesgo Vial Accidental</span>
                  <span class="bmt-val" id="bm-val-risk">15.0x PELIGRO</span>
                </div>
                <div class="bmt-track"><div class="bmt-bar alert" id="bm-bar-risk" style="width: 95%;"></div></div>
                <div class="bmt-sub" id="bm-sub-risk">Probabilidad Crítica de Microsueño</div>
              </div>

            </div>

            <!-- Protocolo Gráfico en 3 Tarjetas -->
            <div class="visual-protocol-section">
              <div class="vp-section-title">PROTOCOLO VISUAL SG-SST • DESCOMPRESIÓN DIARIA</div>
              <div class="vp-cards-row">
                
                <div class="vp-card-pill">
                  <div class="vp-badge">45 MIN</div>
                  <div class="vp-pill-title">Corte de Pantallas</div>
                  <div class="vp-pill-desc">Apagar celular y luz azul para liberar melatonina.</div>
                </div>

                <div class="vp-card-pill">
                  <div class="vp-badge">7-8 H</div>
                  <div class="vp-pill-title">Sueño Reparador</div>
                  <div class="vp-pill-desc">Ciclos continuos Delta y REM para regeneración celular completa.</div>
                </div>

                <div class="vp-card-pill">
                  <div class="vp-badge">18°C</div>
                  <div class="vp-pill-title">Habitación Fresca</div>
                  <div class="vp-pill-desc">Caída térmica requerida para inducir sueño Delta.</div>
                </div>

              </div>
            </div>

          </div>

        </div>
      </div>
    </section>

    </main>

  <!-- BOT CEREBRITO SST Y NARRACIÓN COLOMBIANA -->
  

  <!-- BARRA INFERIOR DE NAVEGACIÓN -->
  <footer class="antigravity-bottom-dock" role="contentinfo">
    <div class="dock-stage-counter" id="dock-stage-counter">
      ETAPA 1 DE 5 • CEREBRO 3D INTERACTIVO
    </div>

    <div class="dock-nav-btns">
      <button type="button" class="dock-btn" id="btn-dock-global-prev">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
        <span>Anterior</span>
      </button>
      <button type="button" class="dock-btn is-primary" id="btn-dock-global-next">
        <span>Siguiente</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
      </button>
    </div>
  </footer>

  <!-- =========================================================================
       SCRIPTS: CEREBRO 3D ROTATORIO Y SIMULADOR PROCEDURAL VIAL
       ========================================================================= -->
  <script>
    /* =========================================================================
       1. VARIABLES GLOBALES Y NAVEGACIÓN
       ========================================================================= */
    let currentStageIndex = 0;
    const stageLayers = document.querySelectorAll(".stage-layer");
    const stagePills = document.querySelectorAll(".stage-step-pill");
    const dockStageIndicator = document.getElementById("dock-stage-counter");

    const stageTitles = [
      "ETAPA 1 DE 5 • CEREBRO 3D INTERACTIVO",
      "ETAPA 2 DE 5 • RESPIRACIÓN 4-7-8 CON APNEA",
      "ETAPA 3 DE 5 • SIMULADOR VIAL POV",
      "ETAPA 4 DE 5 • DECISIONES DE TURNO",
      "ETAPA 5 DE 5 • FISIOLOGÍA DEL ESTRÉS Y RECUPERACIÓN"
    ];

    /* =========================================================================
       2. PARTÍCULAS ANTIGRAVITY EN FONDO CLARO (#eef2f6)
       ========================================================================= */
    const bgCanvas = document.getElementById("antigravity-particles-canvas");
    const bgctx = bgCanvas.getContext("2d");
    let bgParticles = [];
    let mousePos = { x: window.innerWidth / 2, y: window.innerHeight / 2 };

    function initBgParticles() {
      bgCanvas.width = window.innerWidth;
      bgCanvas.height = window.innerHeight;
      bgParticles = [];
      const count = Math.min(75, Math.floor((bgCanvas.width * bgCanvas.height) / 16000));
      const colorPalettes = [
        { fill: "rgba(2, 132, 199, 0.38)", halo: "rgba(2, 132, 199, 0.08)", line: "rgba(2, 132, 199, 0.14)" },
        { fill: "rgba(79, 70, 229, 0.32)", halo: "rgba(79, 70, 229, 0.07)", line: "rgba(79, 70, 229, 0.12)" },
        { fill: "rgba(5, 150, 105, 0.32)", halo: "rgba(5, 150, 105, 0.06)", line: "rgba(5, 150, 105, 0.10)" }
      ];
      for (let i = 0; i < count; i++) {
        const col = colorPalettes[i % colorPalettes.length];
        bgParticles.push({
          x: Math.random() * bgCanvas.width,
          y: Math.random() * bgCanvas.height,
          vx: (Math.random() - 0.5) * 0.38,
          vy: (Math.random() - 0.5) * 0.38,
          baseR: Math.random() * 2.0 + 1.3,
          phase: Math.random() * Math.PI * 2,
          color: col
        });
      }
    }
    initBgParticles();

    window.addEventListener("mousemove", (e) => {
      mousePos.x = e.clientX;
      mousePos.y = e.clientY;
    }, { passive: true });

    let bgAnimTime = 0;
    function renderBgParticles() {
      bgctx.clearRect(0, 0, bgCanvas.width, bgCanvas.height);
      const w = bgCanvas.width;
      const h = bgCanvas.height;
      bgAnimTime += 0.015;

      for (let i = 0; i < bgParticles.length; i++) {
        const p = bgParticles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = w;
        else if (p.x > w) p.x = 0;
        if (p.y < 0) p.y = h;
        else if (p.y > h) p.y = 0;

        const dx = mousePos.x - p.x;
        const dy = mousePos.y - p.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 130) {
          const force = (130 - dist) / 130;
          p.x -= (dx / dist) * force * 1.8;
          p.y -= (dy / dist) * force * 1.8;
        }

        const currentR = p.baseR + Math.sin(bgAnimTime + p.phase) * 0.45;

        // Halo bio-luminiscente suave
        bgctx.beginPath();
        bgctx.arc(p.x, p.y, currentR * 2.8, 0, Math.PI * 2);
        bgctx.fillStyle = p.color.halo;
        bgctx.fill();

        // Nodo central
        bgctx.beginPath();
        bgctx.arc(p.x, p.y, currentR, 0, Math.PI * 2);
        bgctx.fillStyle = p.color.fill;
        bgctx.fill();

        for (let j = i + 1; j < bgParticles.length; j++) {
          const p2 = bgParticles[j];
          const d2 = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (d2 < 105) {
            const alpha = (1 - d2 / 105) * 0.15;
            bgctx.strokeStyle = `rgba(2, 132, 199, ${alpha})`;
            bgctx.lineWidth = 1;
            bgctx.beginPath();
            bgctx.moveTo(p.x, p.y);
            bgctx.lineTo(p2.x, p2.y);
            bgctx.stroke();
          }
        }
      }
      requestAnimationFrame(renderBgParticles);
    }
    renderBgParticles();

    /* =========================================================================
       3. FASE 1: CEREBRO ANATÓMICO 3D INTERACTIVO (ROTACIÓN TOTAL Y VISTA INTERNA)
       ========================================================================= */
    const brainCanvas = document.getElementById("anatomical-brain-canvas");
    const bctx = brainCanvas.getContext("2d");

    let brainBiometricState = "calm"; // "calm" | "stress"
    let isInnerViewActive = false;     // Corte sagital para mirar por dentro
    let brainZoom = 1.0;

    // Ángulos de rotación 3D (arrastre libre)
    let bRotY = 0.35; // Rotación Azimut
    let bRotX = 0.18; // Inclinación Elevación
    let isDraggingBrain = false;
    let lastBx = 0, lastBy = 0;

    let brain3DNodes = [];
    let brain3DAxons = [];
    let actionPotentials = []; // Pulsos de luz viajando en 3D

    function initTrue3DBrain() {
      brain3DNodes = [];
      brain3DAxons = [];
      actionPotentials = [];

      // 1. Corteza Cerebral Externa: Dos Hemisferios con circunvoluciones y cisuras
      // Lóbulos: Frontal, Parietal, Occipital, Temporal
      for (let i = 0; i < 260; i++) {
        const u = Math.random();
        const v = Math.random();
        const theta = u * 2.0 * Math.PI;
        const phi = Math.acos(2.0 * v - 1.0);

        // Geometría orgánica ovoide cerebral
        const r_base = 115.0 * Math.pow(Math.random(), 0.28);
        const sulci = 1.0 + 0.14 * Math.sin(6 * theta) * Math.cos(5 * phi) + 0.08 * Math.cos(10 * phi);
        const r = r_base * sulci;

        let x = r * Math.sin(phi) * Math.cos(theta);
        let y = r * Math.sin(phi) * Math.sin(theta) * 0.74; // achatado vertical
        let z = r * Math.cos(phi) * 1.18;                  // alargado anterior-posterior

        // Depresión inferior para tronco y cerebelo
        if (z < -20) y += 10;
        else if (z > 35) y -= 8;

        // Separación interhemisférica
        const hemi = (x >= 0) ? 1 : -1;
        x += hemi * 14;

        // Asignación de región anatómica
        let region = "cortex";
        if (z > 40) region = "frontal";
        else if (z < -35 && y < 15) region = "occipital";
        else if (Math.abs(x) > 55 && y > 10) region = "temporal";
        else if (y < -30) region = "parietal";

        brain3DNodes.push({
          baseX: x, baseY: y, baseZ: z,
          x, y, z,
          region,
          isDeep: false,
          phase: Math.random() * Math.PI * 2,
          radius: Math.random() * 2.0 + 1.8,
          speed: 0.002 + Math.random() * 0.003
        });
      }

      // 2. Cerebelo (Posterior Inferior con estriaciones laminares)
      for (let i = 0; i < 65; i++) {
        const ang = Math.random() * Math.PI * 2;
        const r = 42 * Math.pow(Math.random(), 0.5);
        const side = Math.random() > 0.5 ? 20 : -20;
        const x = r * Math.cos(ang) * 1.1 + side;
        const y = 52 + (Math.random() - 0.5) * 22;
        const z = -48 + (Math.random() - 0.5) * 28;

        brain3DNodes.push({
          baseX: x, baseY: y, baseZ: z,
          x, y, z,
          region: "cerebellum",
          isDeep: false,
          phase: Math.random() * Math.PI * 2,
          radius: Math.random() * 1.8 + 1.5,
          speed: 0.003
        });
      }

      // 3. Tronco Encefálico (Columna inferior central)
      for (let i = 0; i < 35; i++) {
        const t = Math.random();
        const y = 45 + t * 65;
        const rad = 15 * (1.0 - t * 0.35);
        const ang = Math.random() * Math.PI * 2;
        const x = rad * Math.cos(ang);
        const z = -8 + rad * Math.sin(ang) * 0.8;

        brain3DNodes.push({
          baseX: x, baseY: y, baseZ: z,
          x, y, z,
          region: "stem",
          isDeep: true,
          phase: Math.random() * Math.PI * 2,
          radius: Math.random() * 2.0 + 1.6,
          speed: 0.0025
        });
      }

      // 4. ESTRUCTURAS INTERNAS PROFUNDAS ("MIRAR POR ADENTRO"):
      // Amígdala (Bilateral profunda, centro del estrés y cortisol)
      for (let side of [-28, 28]) {
        for (let i = 0; i < 18; i++) {
          const ang = Math.random() * Math.PI * 2;
          const r = 14 * Math.random();
          brain3DNodes.push({
            baseX: side + Math.cos(ang) * r,
            baseY: 22 + Math.sin(ang) * r * 0.8,
            baseZ: 14 + (Math.random() - 0.5) * 12,
            region: "amygdala",
            isDeep: true,
            phase: Math.random() * Math.PI * 2,
            radius: Math.random() * 2.6 + 2.2,
            speed: 0.004
          });
        }
      }

      // Glándula Pineal (Central profunda, fábrica de melatonina y descanso)
      for (let i = 0; i < 14; i++) {
        const ang = Math.random() * Math.PI * 2;
        const r = 9 * Math.random();
        brain3DNodes.push({
          baseX: Math.cos(ang) * r * 0.9,
          baseY: 8 + Math.sin(ang) * r * 0.9,
          baseZ: -18 + (Math.random() - 0.5) * 8,
          region: "pineal",
          isDeep: true,
          phase: Math.random() * Math.PI * 2,
          radius: Math.random() * 3.0 + 2.2,
          speed: 0.002
        });
      }

      // Hipocampo (Arcos bilaterales de consolidación del sueño)
      for (let side of [-1, 1]) {
        for (let i = 0; i < 20; i++) {
          const t = i / 20;
          const arcAng = t * Math.PI * 0.85;
          const hx = side * (24 + Math.sin(arcAng) * 16);
          const hy = 24 - Math.cos(arcAng) * 10;
          const hz = 12 - t * 32;
          brain3DNodes.push({
            baseX: hx + (Math.random() - 0.5) * 6,
            baseY: hy + (Math.random() - 0.5) * 6,
            baseZ: hz + (Math.random() - 0.5) * 6,
            region: "hippocampus",
            isDeep: true,
            phase: Math.random() * Math.PI * 2,
            radius: 2.2,
            speed: 0.002
          });
        }
      }

      // 5. TERMINACIONES NERVIOSAS EXTERIORES (ARBORIZACIONES 3D RADIALES)
      for (let i = 0; i < 50; i++) {
        const theta = Math.random() * Math.PI * 2;
        const phi = Math.random() * Math.PI;
        const rad = 138 + Math.random() * 25;
        const tx = rad * Math.sin(phi) * Math.cos(theta);
        const ty = rad * Math.sin(phi) * Math.sin(theta) * 0.75;
        const tz = rad * Math.cos(phi) * 1.15;

        brain3DNodes.push({
          baseX: tx, baseY: ty, baseZ: tz,
          x: tx, y: ty, z: tz,
          region: "nerve_terminal",
          isDeep: false,
          phase: Math.random() * Math.PI * 2,
          radius: Math.random() * 2.8 + 1.8,
          speed: 0.003
        });
      }

      // 6. Conectar nodos con fibras axonales tridimensionales
      for (let i = 0; i < brain3DNodes.length; i++) {
        const a = brain3DNodes[i];
        for (let j = i + 1; j < brain3DNodes.length; j++) {
          const b = brain3DNodes[j];
          const d = Math.hypot(a.baseX - b.baseX, a.baseY - b.baseY, a.baseZ - b.baseZ);
          // Conexión por vecindad
          if (d < 32 && (a.isDeep === b.isDeep || d < 22)) {
            brain3DAxons.push({ a: i, b: j, dist: d });
            // Agregar potenciales de acción
            if (Math.random() < 0.22) {
              actionPotentials.push({
                axonIdx: brain3DAxons.length - 1,
                progress: Math.random(),
                speed: 0.35 + Math.random() * 0.45
              });
            }
          }
        }
      }
    }
    initTrue3DBrain();

    // Eventos de arrastre 3D libre e interactivo
    const brainBox = document.getElementById("brain-container-box");
    if (brainBox) {
      brainBox.addEventListener("mousedown", (e) => {
        isDraggingBrain = true;
        lastBx = e.clientX;
        lastBy = e.clientY;
      });
      window.addEventListener("mousemove", (e) => {
        if (!isDraggingBrain) return;
        const dx = e.clientX - lastBx;
        const dy = e.clientY - lastBy;
        bRotY += dx * 0.009;
        bRotX += dy * 0.009;
        // Limitar elevación vertical
        bRotX = Math.max(-1.3, Math.min(1.3, bRotX));
        lastBx = e.clientX;
        lastBy = e.clientY;
      }, { passive: true });
      window.addEventListener("mouseup", () => {
        isDraggingBrain = false;
      });

      // Zoom con rueda del mouse
      brainBox.addEventListener("wheel", (e) => {
        e.preventDefault();
        brainZoom += (e.deltaY < 0 ? 0.08 : -0.08);
        brainZoom = Math.max(0.65, Math.min(2.1, brainZoom));
      }, { passive: false });

      // Soporte táctil para Celular y Tablet en el Cerebro 3D
      let lastTouchX = 0, lastTouchY = 0;
      let initialPinchDist = 0;

      brainCanvas.addEventListener("touchstart", (e) => {
        if (e.touches.length === 1) {
          isDraggingBrain = true;
          lastTouchX = e.touches[0].clientX;
          lastTouchY = e.touches[0].clientY;
        } else if (e.touches.length === 2) {
          initialPinchDist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
          );
        }
      }, { passive: true });

      brainCanvas.addEventListener("touchmove", (e) => {
        if (e.touches.length === 1 && isDraggingBrain) {
          const dx = e.touches[0].clientX - lastTouchX;
          const dy = e.touches[0].clientY - lastTouchY;
          bRotY += dx * 0.008;
          bRotX += dy * 0.008;
          bRotX = Math.max(-1.1, Math.min(1.1, bRotX));
          lastTouchX = e.touches[0].clientX;
          lastTouchY = e.touches[0].clientY;
        } else if (e.touches.length === 2 && initialPinchDist > 0) {
          const currentDist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
          );
          const zoomFactor = currentDist / initialPinchDist;
          brainZoom = Math.max(0.65, Math.min(2.1, brainZoom * (1 + (zoomFactor - 1) * 0.05)));
          targetBrainZoom = brainZoom;
          initialPinchDist = currentDist;
        }
      }, { passive: true });

      brainCanvas.addEventListener("touchend", () => {
        isDraggingBrain = false;
        initialPinchDist = 0;
      }, { passive: true });
    }

    // =========================================================================
    // RUTA NEURAL GUIADA DEL CEREBRO 3D (SECUENCIA SIN SUPERPOSICIÓN DE AUDIO)
    // =========================================================================
    let brainTourStep = 1;
    let isBrainTourPlaying = true;
    let brainTourTimer = null;
    let isBrainTourActive = true;
    let targetBrainZoom = 1.0;
    let targetRotX = 0.18;
    let targetRotY = 0.35;

    const brainTourNarrations = {
      1: "Paso 1: Estado Delta Exterior. Con ondas lentas de 2.1 hercios, el cerebro limpia toxinas celulares y repara tus redes neuronales tras la jornada.",
      2: "Paso 2: Interior Límbico. Al ingresar a las estructuras profundas, la amígdala y el hipocampo reposan en calma, consolidando la memoria y el descanso profundo.",
      3: "Paso 3: Sobrecarga por Estrés. Ante la tensión acumulada, la amígdala se hiperactiva a 28 hercios desde adentro, inundando el organismo de cortisol y bloqueando la conciliación del sueño.",
      4: "Paso 4: Fatiga Cortical Exterior. En el exterior, la corteza frontal queda agotada de adenosina. Sin descompresión, el riesgo de microsueño al volante aumenta drásticamente. Pasamos ahora al ejercicio de respiración para desactivar este estrés."
    };

    function stopBrainTourAudio() {
      stopAllSomniAudio();
    }

    function setBrainTourStep(step, userTriggered = false) {
      stopBrainTourAudio();
      brainTourStep = Math.max(1, Math.min(4, step));

      // Actualizar botones de pasos
      for (let s = 1; s <= 4; s++) {
        const btn = document.getElementById("btour-step-" + s);
        if (btn) {
          btn.classList.toggle("is-active", s === brainTourStep);
          btn.classList.toggle("is-step-stress", (s === 3 || s === 4) && s === brainTourStep);
        }
      }

      // Configuración cinemática y fisiológica según el paso
      const bState = document.getElementById("b-state");
      const bFreq = document.getElementById("b-freq");
      const bSys = document.getElementById("b-sys");
      const bMel = document.getElementById("b-mel");

      if (brainTourStep === 1) {
        // Delta Exterior
        targetBrainZoom = 1.0;
        isInnerViewActive = false;
        brainBiometricState = "calm";
        targetRotX = 0.18;
        targetRotY = 0.35;

        if (bState) { bState.textContent = "ONDAS DELTA (REPARACIÓN)"; bState.style.color = "var(--cyan-brand)"; }
        if (bFreq) { bFreq.textContent = "2.1 Hz (DELTA PROFUNDA)"; bFreq.style.color = "var(--text-title)"; }
        if (bSys) { bSys.textContent = "LAVADO GLINFÁTICO ACTIVO"; bSys.style.color = "var(--emerald-safe)"; }
        if (bMel) { bMel.textContent = "ALTA (92 pg/mL)"; bMel.style.color = "var(--gold-accent)"; }
      } 
      else if (brainTourStep === 2) {
        // Interior Límbico Calma
        targetBrainZoom = 1.45;
        isInnerViewActive = true;
        brainBiometricState = "calm";
        targetRotX = 0.12;
        targetRotY = 0.60;

        if (bState) { bState.textContent = "NÚCLEO LÍMBICO EN REPOSO"; bState.style.color = "var(--indigo-brand)"; }
        if (bFreq) { bFreq.textContent = "2.4 Hz (SUEÑO REPARADOR)"; bFreq.style.color = "var(--text-title)"; }
        if (bSys) { bSys.textContent = "AMÍGDALA SERENA / HIPOCAMPO"; bSys.style.color = "var(--emerald-safe)"; }
        if (bMel) { bMel.textContent = "ÓPTIMA EN GLÁNDULA PINEAL"; bMel.style.color = "var(--gold-accent)"; }
      }
      else if (brainTourStep === 3) {
        // Sobrecarga Interior
        targetBrainZoom = 1.45;
        isInnerViewActive = true;
        brainBiometricState = "stress";
        targetRotX = 0.14;
        targetRotY = 0.75;

        if (bState) { bState.textContent = "HIPERACTIVACIÓN LÍMBICA"; bState.style.color = "var(--red-alert)"; }
        if (bFreq) { bFreq.textContent = "28.4 Hz (BETA ALTA / ESTRÉS)"; bFreq.style.color = "var(--amber-alert)"; }
        if (bSys) { bSys.textContent = "AMÍGDALA HIPERACTIVA"; bSys.style.color = "var(--red-alert)"; }
        if (bMel) { bMel.textContent = "BLOQUEADA POR CORTISOL"; bMel.style.color = "var(--red-alert)"; }
      }
      else if (brainTourStep === 4) {
        // Fatiga Cortical Exterior
        targetBrainZoom = 1.05;
        isInnerViewActive = false;
        brainBiometricState = "stress";
        targetRotX = 0.18;
        targetRotY = 0.40;

        if (bState) { bState.textContent = "AGOTAMIENTO CORTICAL CRÍTICO"; bState.style.color = "var(--red-alert)"; }
        if (bFreq) { bFreq.textContent = "28.0 Hz (FATIGA CRÓNICA)"; bFreq.style.color = "var(--amber-alert)"; }
        if (bSys) { bSys.textContent = "DRENAJE BLOQUEADO / ADENOSINA"; bSys.style.color = "var(--red-alert)"; }
        if (bMel) { bMel.textContent = "SUPRIMIDA (8 pg/mL)"; bMel.style.color = "var(--red-alert)"; }
      }

      // Actualizar estado habilitado/deshabilitado de botones
      const btnPrev = document.getElementById("btn-tour-prev");
      const btnNext = document.getElementById("btn-tour-next");
      if (btnPrev) {
        btnPrev.classList.toggle("is-disabled", brainTourStep === 1);
        btnPrev.disabled = (brainTourStep === 1);
      }
      if (btnNext) {
        btnNext.classList.toggle("is-disabled", brainTourStep === 4);
        btnNext.disabled = (brainTourStep === 4);
      }

      // Reproducción de narración con avance encadenado y transición automática
      const tourAudioKey = (brainTourStep === 4) ? "brain_tour_4_trans" : ("brain_tour_" + brainTourStep);
      playSalomeAudio(tourAudioKey, brainTourNarrations[brainTourStep], () => {
        if (isBrainTourPlaying && currentStageIndex === 0 && brainTourStep < 4) {
          brainTourTimer = setTimeout(() => {
            if (isBrainTourPlaying && currentStageIndex === 0) {
              setBrainTourStep(brainTourStep + 1);
            }
          }, 1500);
        } else if (brainTourStep === 4) {
          if (isBrainTourPlaying && currentStageIndex === 0) {
            // Transición automática solicitada por el usuario hacia respiración
            brainTourTimer = setTimeout(() => {
              if (isBrainTourPlaying && currentStageIndex === 0) {
                isBrainTourPlaying = false;
                updateTourPlayPauseBtnUI();
                goToStage(1);
              }
            }, 1200);
          } else {
            isBrainTourPlaying = false;
            updateTourPlayPauseBtnUI();
            const btnBreath = document.getElementById("btn-start-exp-breath");
            if (btnBreath) {
              btnBreath.style.boxShadow = "0 0 16px rgba(2, 132, 199, 0.6)";
            }
          }
        }
      });
    }

    function updateTourPlayPauseBtnUI() {
      const lbl = document.getElementById("label-tour-play-pause");
      const icon = document.getElementById("icon-tour-play-pause");
      const heroLbl = document.getElementById("label-hero-tour-toggle");

      if (isBrainTourPlaying) {
        if (lbl) lbl.textContent = "Pausar";
        if (heroLbl) heroLbl.textContent = "Pausar Ruta Guiada";
        if (icon) icon.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>';
      } else {
        if (lbl) lbl.textContent = (brainTourStep === 4 ? "Repetir" : "Reanudar");
        if (heroLbl) heroLbl.textContent = (brainTourStep === 4 ? "Repetir Ruta Guiada" : "Reanudar Ruta Guiada");
        if (icon) icon.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"/></svg>';
      }
    }

    function toggleBrainTourPlayPause() {
      if (isBrainTourPlaying) {
        isBrainTourPlaying = false;
        stopBrainTourAudio();
        updateTourPlayPauseBtnUI();
      } else {
        isBrainTourPlaying = true;
        updateTourPlayPauseBtnUI();
        if (brainTourStep === 4) {
          setBrainTourStep(1, true);
        } else {
          setBrainTourStep(brainTourStep, true);
        }
      }
    }

    function brainTourNext() {
      if (brainTourStep < 4) {
        setBrainTourStep(brainTourStep + 1, true);
      } else {
        setBrainTourStep(1, true);
      }
    }

    function brainTourPrev() {
      if (brainTourStep > 1) {
        setBrainTourStep(brainTourStep - 1, true);
      }
    }

    function restartBrainTour() {
      isBrainTourPlaying = true;
      updateTourPlayPauseBtnUI();
      setBrainTourStep(1, true);
    }

    let lastBrainRenderTime = 0;

    function render3DInteractiveBrain(now) {
      if (!brainCanvas || !bctx) return;
      const w = brainCanvas.width;
      const h = brainCanvas.height;
      bctx.clearRect(0, 0, w, h);

      if (!lastBrainRenderTime) lastBrainRenderTime = now;
      const deltaSec = Math.min(0.08, (now - lastBrainRenderTime) / 1000);
      lastBrainRenderTime = now;

      // Rotación automática suave cuando no se arrastra
      if (!isDraggingBrain) {
        bRotY += (brainBiometricState === "stress" ? 0.005 : 0.0025);
      }

      // Suavizado cinemático de cámara durante la ruta guiada
      brainZoom += (targetBrainZoom - brainZoom) * 0.07;
      bRotX += (targetRotX - bRotX) * 0.07;

      const cx = w / 2;
      const cy = h * 0.44;
      const baseScale = Math.min(w, h) * 0.0024 * brainZoom;
      const fov = 420;

      const cosY = Math.cos(bRotY), sinY = Math.sin(bRotY);
      const cosX = Math.cos(bRotX), sinX = Math.sin(bRotX);

      const isStress = (brainBiometricState === "stress");
      const pulseMultiplier = isStress ? 4.5 : 1.0;

      // 1. Proyectar nodos cerebrales 3D a 2D
      const projectedNodes = [];
      for (let i = 0; i < brain3DNodes.length; i++) {
        const n = brain3DNodes[i];

        // Pulso fisiológico
        const pulse = 1.0 + Math.sin(now * n.speed * pulseMultiplier + n.phase) * (isStress ? 0.08 : 0.035);
        let bx = n.baseX * pulse;
        let by = n.baseY * pulse;
        let bz = n.baseZ * pulse;

        // Si la vista interna está activa, abrimos los hemisferios lateralmente para mirar el interior
        if (isInnerViewActive && !n.isDeep) {
          const hemiSign = (n.baseX >= 0) ? 1 : -1;
          bx += hemiSign * 24; // Desplazamiento lateral de los hemisferios
        }

        // Rotación Yaw (Y)
        const x1 = bx * cosY - bz * sinY;
        const z1 = bx * sinY + bz * cosY;

        // Rotación Pitch (X)
        const y2 = by * cosX - z1 * sinX;
        const z2 = by * sinX + z1 * cosX;

        // Proyección perspectiva
        const dist = fov / (fov + z2 * baseScale);
        const px = cx + x1 * baseScale * dist;
        const py = cy + y2 * baseScale * dist;

        projectedNodes.push({
          idx: i,
          x: px, y: py, z: z2,
          radius: Math.max(1.0, n.radius * baseScale * 0.8 * dist),
          region: n.region,
          isDeep: n.isDeep,
          dist
        });
      }

      // Ordenar por profundidad Z (Pintor)
      projectedNodes.sort((a, b) => b.z - a.z);

      // 2. DIBUJAR CAPA ENVOLVENTE ANATÓMICA TRASLÚCIDA (CASCARÓN DE LOS LÓBULOS)
      draw3DAnatomicalShell(bctx, cx, cy, cosY, sinY, cosX, sinX, baseScale, fov, isStress, isInnerViewActive);

      // 3. DIBUJAR FIBRAS AXONALES 3D
      bctx.lineWidth = isStress ? 1.2 : 0.85;
      for (let i = 0; i < brain3DAxons.length; i++) {
        const axon = brain3DAxons[i];
        const p1 = projectedNodes.find(n => n.idx === axon.a);
        const p2 = projectedNodes.find(n => n.idx === axon.b);
        if (!p1 || !p2) continue;

        // Opacidad de corteza vs interior
        let alpha = 0.18;
        if (isInnerViewActive) {
          alpha = (p1.isDeep || p2.isDeep) ? 0.45 : 0.08;
        }

        if (isStress) {
          bctx.strokeStyle = `rgba(239, 68, 68, ${alpha})`;
        } else {
          bctx.strokeStyle = `rgba(2, 132, 199, ${alpha})`;
        }

        bctx.beginPath();
        bctx.moveTo(p1.x, p1.y);
        bctx.lineTo(p2.x, p2.y);
        bctx.stroke();
      }

      // 4. POTENCIALES DE ACCIÓN (CHISPAS DE LUZ VIAJANDO POR LOS AXONES)
      for (let i = 0; i < actionPotentials.length; i++) {
        const ap = actionPotentials[i];
        const axon = brain3DAxons[ap.axonIdx];
        if (!axon) continue;
        const p1 = projectedNodes.find(n => n.idx === axon.a);
        const p2 = projectedNodes.find(n => n.idx === axon.b);
        if (!p1 || !p2) continue;

        ap.progress = (ap.progress + deltaSec * ap.speed * (isStress ? 3.0 : 1.0)) % 1.0;
        const sparkX = p1.x + (p2.x - p1.x) * ap.progress;
        const sparkY = p1.y + (p2.y - p1.y) * ap.progress;

        bctx.beginPath();
        bctx.arc(sparkX, sparkY, isStress ? 2.4 : 1.6, 0, Math.PI * 2);
        bctx.fillStyle = isStress ? "#fef08a" : "#FFFFFF";
        bctx.fill();
      }

      // 5. DIBUJAR NODOS Y TERMINACIONES NERVIOSAS 3D
      for (let i = 0; i < projectedNodes.length; i++) {
        const p = projectedNodes[i];

        // Definir color según estado y región anatómica
        let color = "rgba(2, 132, 199, 0.9)";
        let glow = "rgba(56, 189, 248, 0.35)";

        if (isStress) {
          if (p.region === "amygdala") {
            color = "#ef4444";
            glow = "rgba(239, 68, 68, 0.6)";
          } else if (p.region === "nerve_terminal") {
            color = "#f59e0b";
            glow = "rgba(245, 158, 11, 0.55)";
          } else {
            color = "#ea580c";
            glow = "rgba(234, 88, 12, 0.4)";
          }
        } else {
          if (p.region === "pineal") {
            color = "#d97706";
            glow = "rgba(217, 119, 6, 0.5)";
          } else if (p.region === "cerebellum") {
            color = "#059669";
            glow = "rgba(16, 185, 129, 0.45)";
          } else if (p.region === "nerve_terminal") {
            color = "#00f0ff";
            glow = "rgba(0, 240, 255, 0.55)";
          }
        }

        // Si la vista interior está activa, atenuamos nodos de corteza y resaltamos el interior
        let finalAlpha = 1.0;
        if (isInnerViewActive && !p.isDeep && p.region !== "nerve_terminal") {
          finalAlpha = 0.22;
        }

        // Halo luminoso
        bctx.beginPath();
        bctx.arc(p.x, p.y, p.radius * 2.2, 0, Math.PI * 2);
        bctx.fillStyle = glow.replace(/[\d\.]+\)$/, `${finalAlpha * 0.4})`);
        bctx.fill();

        // Núcleo del nodo sináptico
        bctx.beginPath();
        bctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        bctx.fillStyle = color;
        bctx.globalAlpha = finalAlpha;
        bctx.fill();
        bctx.globalAlpha = 1.0;
      }

      requestAnimationFrame(render3DInteractiveBrain);
    }

    // Dibuja la silueta anatómica 3D translúcida de los lóbulos
    function draw3DAnatomicalShell(ctx, cx, cy, cosY, sinY, cosX, sinX, scale, fov, isStress, isInner) {
      const hemispheres = [-1, 1];
      const shellAlpha = isInner ? 0.05 : 0.16;
      const strokeAlpha = isInner ? 0.12 : 0.35;
      const strokeColor = isStress ? `rgba(220, 38, 38, ${strokeAlpha})` : `rgba(2, 132, 199, ${strokeAlpha})`;
      const fillColor = isStress ? `rgba(220, 38, 38, ${shellAlpha})` : `rgba(2, 132, 199, ${shellAlpha})`;

      for (let h = 0; h < hemispheres.length; h++) {
        const hemi = hemispheres[h];
        const perimeter = [];
        const steps = 30;

        for (let s = 0; s < steps; s++) {
          const t = (s / steps) * Math.PI * 2;
          const rx = 48 + 6 * Math.sin(3 * t);
          const ry = (t > Math.PI ? 32 : 56) * (1 + 0.08 * Math.cos(4 * t));
          const rz = (Math.cos(t) > 0 ? 58 : 48);

          let bx = hemi * (15 + rx * Math.abs(Math.sin(t) * 0.9));
          let by = -ry * Math.cos(t) + 6;
          let bz = rz * Math.sin(t);

          if (isInner) bx += hemi * 24;

          const x1 = bx * cosY - bz * sinY;
          const z1 = bx * sinY + bz * cosY;
          const y2 = by * cosX - z1 * sinX;
          const z2 = by * sinX + z1 * cosX;

          const dist = fov / (fov + z2 * scale);
          perimeter.push({
            x: cx + x1 * scale * dist,
            y: cy + y2 * scale * dist
          });
        }

        ctx.beginPath();
        ctx.moveTo(perimeter[0].x, perimeter[0].y);
        for (let i = 1; i < perimeter.length; i++) {
          const prev = perimeter[i - 1];
          const curr = perimeter[i];
          ctx.quadraticCurveTo(prev.x, prev.y, (prev.x + curr.x) / 2, (prev.y + curr.y) / 2);
        }
        ctx.closePath();

        ctx.fillStyle = fillColor;
        ctx.fill();
        ctx.strokeStyle = strokeColor;
        ctx.lineWidth = 1.8;
        ctx.stroke();
      }
    }

    function setBrainStateGlobal(state) {
      // Compatibilidad con invocaciones externas
      if (state === "stress") {
        setBrainTourStep(3, true);
      } else {
        setBrainTourStep(1, true);
      }
    }

    /* =========================================================================
       4. FASE 2: BIOMECÁNICA PULMONAR 4-7-8 CON DETENCIÓN TOTAL (APNEA 7s)
       ========================================================================= */
    const breathCanvas = document.getElementById("breath-rings-canvas");
    const brctx = breathCanvas.getContext("2d");
    const holdPill = document.getElementById("breath-hold-pill");

    let isBreathingActive = false;
    let isBreathingIntro = true;
    let breathCycleCount = 1;
    let breathTimeInCycle = 0;
    let breathPhase = "intro";
    let breathCountdown = 4;
    let breathExpansion = 0.0;
    let lastBreathTimestamp = 0;
    let prevBreathPhase = "intro";

    let airFlowParticles = [];
    function initAirFlowParticles() {
      airFlowParticles = [];
      for (let i = 0; i < 60; i++) {
        airFlowParticles.push({
          progress: Math.random(),
          side: Math.random() > 0.5 ? 1 : -1,
          branchIdx: Math.floor(Math.random() * 3),
          speed: 0.18 + Math.random() * 0.22,
          radius: Math.random() * 1.8 + 1.2
        });
      }
    }
    initAirFlowParticles();

    function renderHolographicLungs(now) {
      if (!breathCanvas || !brctx) return;
      const w = breathCanvas.width;
      const h = breathCanvas.height;
      brctx.clearRect(0, 0, w, h);

      const cx = w / 2;
      const cy = h / 2 - 10;

      if (!lastBreathTimestamp) lastBreathTimestamp = now;
      const deltaSec = Math.min(0.08, (now - lastBreathTimestamp) / 1000);
      lastBreathTimestamp = now;

      const cycleDuration = 19.0;
      if (isBreathingIntro) {
        breathExpansion = 0.18 + 0.05 * Math.sin(now * 0.002);
        breathPhase = "intro";
        if (holdPill) holdPill.classList.remove("is-active");
      } else if (isBreathingActive) {
        const nextTime = breathTimeInCycle + deltaSec;
        if (nextTime >= cycleDuration) {
          if (breathCycleCount < 3) {
            breathCycleCount++;
            breathTimeInCycle = 0;
            breathPhase = "inhale";
            prevBreathPhase = "inhale";
            playInhaleSound();
            triggerBreathingVocalCue("inhale");
          } else {
            // Se completaron los 3 ciclos exactos -> transición automática al simulador vial
            breathTimeInCycle = cycleDuration;
            finishBreathingAndTransitionToSimulator();
          }
        } else {
          breathTimeInCycle = nextTime;
        }

        if (isBreathingActive) {
          if (breathTimeInCycle < 4.0) {
            breathPhase = "inhale";
            breathCountdown = Math.max(1, Math.ceil(4.0 - breathTimeInCycle));
            const t = breathTimeInCycle / 4.0;
            breathExpansion = 0.5 - 0.5 * Math.cos(t * Math.PI);
            if (holdPill) holdPill.classList.remove("is-active");
          } else if (breathTimeInCycle < 11.0) {
            // DETENCIÓN TOTAL Y ABSOLUTA (APNEA 7s EXACTOS)
            breathPhase = "hold";
            breathCountdown = Math.max(1, Math.ceil(11.0 - breathTimeInCycle));
            breathExpansion = 1.0; // BLOQUEADO AL 100%, CERO OSCILACIÓN
            if (holdPill) holdPill.classList.add("is-active");
          } else {
            // EXHALACIÓN CONTROLADA (8s EXACTOS)
            breathPhase = "exhale";
            breathCountdown = Math.max(1, Math.ceil(19.0 - breathTimeInCycle));
            const t = (breathTimeInCycle - 11.0) / 8.0;
            breathExpansion = 0.5 + 0.5 * Math.cos(t * Math.PI);
            if (holdPill) holdPill.classList.remove("is-active");
          }

          if (breathPhase !== prevBreathPhase) {
            if (breathPhase === "inhale") {
              playInhaleSound();
              triggerBreathingVocalCue("inhale");
            } else if (breathPhase === "hold") {
              triggerBreathingVocalCue("hold");
            } else if (breathPhase === "exhale") {
              playExhaleSound();
              triggerBreathingVocalCue("exhale");
            }
            prevBreathPhase = breathPhase;
          }
        }
      }

      updateBreathHUD();

      const lungW = 95 + breathExpansion * 38;
      const lungH = 140 + breathExpansion * 35;
      const ribsExpansion = breathExpansion * 16;

      // 1. TÓRAX Y COSTILLAS
      brctx.strokeStyle = `rgba(56, 189, 248, ${0.18 + breathExpansion * 0.14})`;
      brctx.lineWidth = 2.0;

      brctx.beginPath();
      const shoulderSpread = 240 + ribsExpansion * 0.8;
      brctx.moveTo(cx - shoulderSpread, cy + 180);
      brctx.lineTo(cx - 210 - ribsExpansion * 0.6, cy - 30);
      brctx.quadraticCurveTo(cx - 160, cy - 140, cx - 60, cy - 170);
      brctx.lineTo(cx - 35, cy - 230);
      brctx.lineTo(cx + 35, cy - 230);
      brctx.lineTo(cx + 60, cy - 170);
      brctx.quadraticCurveTo(cx + 160, cy - 140, cx + 210 + ribsExpansion * 0.6, cy - 30);
      brctx.lineTo(cx + shoulderSpread, cy + 180);
      brctx.stroke();

      // Clavículas
      brctx.beginPath();
      brctx.moveTo(cx - 30, cy - 160);
      brctx.quadraticCurveTo(cx - 110, cy - 165 - ribsExpansion * 0.2, cx - 180, cy - 130);
      brctx.moveTo(cx + 30, cy - 160);
      brctx.quadraticCurveTo(cx + 110, cy - 165 - ribsExpansion * 0.2, cx + 180, cy - 130);
      brctx.stroke();

      // Costillas
      brctx.strokeStyle = `rgba(56, 189, 248, ${0.14 + breathExpansion * 0.12})`;
      for (let r = 0; r < 5; r++) {
        const ry = cy - 80 + r * 42;
        const arcSpread = 135 + r * 14 + ribsExpansion;
        brctx.beginPath();
        brctx.moveTo(cx - 24, ry - 14);
        brctx.quadraticCurveTo(cx - arcSpread * 0.7, ry - 6, cx - arcSpread, ry + 16);
        brctx.moveTo(cx + 24, ry - 14);
        brctx.quadraticCurveTo(cx + arcSpread * 0.7, ry - 6, cx + arcSpread, ry + 16);
        brctx.stroke();
      }

      // 2. TRÁQUEA Y BRONQUIOS
      brctx.strokeStyle = "rgba(56, 189, 248, 0.75)";
      brctx.lineWidth = 7.0;
      brctx.lineCap = "round";

      brctx.beginPath();
      brctx.moveTo(cx, cy - 210);
      brctx.lineTo(cx, cy - 80);
      brctx.stroke();

      // Anillos traqueales
      brctx.strokeStyle = "rgba(255, 255, 255, 0.9)";
      brctx.lineWidth = 1.6;
      for (let ty = cy - 200; ty < cy - 85; ty += 14) {
        brctx.beginPath();
        brctx.moveTo(cx - 8, ty);
        brctx.lineTo(cx + 8, ty);
        brctx.stroke();
      }

      // Bifurcación bronquial
      brctx.strokeStyle = "rgba(56, 189, 248, 0.8)";
      brctx.lineWidth = 5.0;
      brctx.beginPath();
      brctx.moveTo(cx, cy - 80);
      brctx.quadraticCurveTo(cx - 24, cy - 65, cx - 44 - breathExpansion * 10, cy - 35);
      brctx.moveTo(cx, cy - 80);
      brctx.quadraticCurveTo(cx + 24, cy - 65, cx + 44 + breathExpansion * 10, cy - 35);
      brctx.stroke();

      // 3. LÓBULOS PULMONARES ANATÓMICOS
      const sides = [-1, 1];
      for (let s = 0; s < sides.length; s++) {
        const side = sides[s];
        const centerLX = cx + side * (82 + breathExpansion * 20);
        const centerLY = cy + 10;

        brctx.beginPath();
        brctx.moveTo(centerLX - side * 22, centerLY - lungH * 0.55);
        brctx.bezierCurveTo(
          centerLX + side * (lungW * 0.95), centerLY - lungH * 0.35,
          centerLX + side * (lungW * 1.05), centerLY + lungH * 0.25,
          centerLX + side * (lungW * 0.75), centerLY + lungH * 0.55
        );
        brctx.bezierCurveTo(
          centerLX + side * (lungW * 0.2), centerLY + lungH * 0.58 + (breathExpansion * 12),
          centerLX - side * (lungW * 0.3), centerLY + lungH * 0.50,
          centerLX - side * (lungW * 0.55), centerLY + lungH * 0.38
        );
        brctx.bezierCurveTo(
          centerLX - side * (lungW * 0.65), centerLY + lungH * 0.1,
          centerLX - side * (lungW * 0.55), centerLY - lungH * 0.25,
          centerLX - side * 22, centerLY - lungH * 0.55
        );
        brctx.closePath();

        const grad = brctx.createRadialGradient(centerLX, centerLY, 20, centerLX, centerLY, lungW * 1.1);
        if (breathPhase === "hold") {
          grad.addColorStop(0, "rgba(16, 185, 129, 0.45)");
          grad.addColorStop(0.7, "rgba(5, 150, 105, 0.28)");
          grad.addColorStop(1, "rgba(4, 120, 87, 0.12)");
        } else {
          grad.addColorStop(0, `rgba(56, 189, 248, ${0.28 + breathExpansion * 0.25})`);
          grad.addColorStop(0.7, `rgba(2, 132, 199, ${0.18 + breathExpansion * 0.18})`);
          grad.addColorStop(1, "rgba(14, 116, 144, 0.08)");
        }
        brctx.fillStyle = grad;
        brctx.fill();

        brctx.strokeStyle = (breathPhase === "hold") ? "rgba(16, 185, 129, 0.85)" : "rgba(56, 189, 248, 0.75)";
        brctx.lineWidth = 2.4;
        brctx.stroke();
      }

      // 4. FLUJO DE PARTÍCULAS:
      // EN RETENER (HOLD) -> CONGELACIÓN TOTAL, CERO MOVIMIENTO
      for (let i = 0; i < airFlowParticles.length; i++) {
        const p = airFlowParticles[i];

        if (breathPhase === "inhale") {
          p.progress = (p.progress + deltaSec * p.speed * 1.25) % 1.0;
        } else if (breathPhase === "exhale") {
          p.progress = (p.progress - deltaSec * p.speed * 1.15 + 1.0) % 1.0;
        }
        // En "hold" NO hay avance de p.progress: congeladas totalmente

        let px = cx, py = cy;
        let pColor = "rgba(56, 189, 248, 0.95)";

        if (p.progress < 0.35) {
          const t = p.progress / 0.35;
          px = cx + Math.sin(t * 12) * 2;
          py = (cy - 210) + t * 130;
        } else if (p.progress < 0.65) {
          const t = (p.progress - 0.35) / 0.30;
          const endBX = cx + p.side * (44 + breathExpansion * 12);
          px = cx + t * (endBX - cx);
          py = (cy - 80) + t * 45;
        } else {
          const t = (p.progress - 0.65) / 0.35;
          const startBX = cx + p.side * (44 + breathExpansion * 12);
          const targetX = startBX + p.side * (p.branchIdx === 0 ? 50 : p.branchIdx === 1 ? 28 : 46);
          const targetY = (cy - 35) + (p.branchIdx === 0 ? 46 : p.branchIdx === 1 ? 95 : 80);
          px = startBX + t * (targetX - startBX);
          py = (cy - 35) + t * (targetY - (cy - 35));
        }

        if (breathPhase === "exhale") {
          pColor = "rgba(251, 191, 36, 0.95)";
        } else if (breathPhase === "hold") {
          pColor = "rgba(16, 185, 129, 0.95)";
        }

        brctx.beginPath();
        brctx.arc(px, py, p.radius * (0.8 + breathExpansion * 0.5), 0, Math.PI * 2);
        brctx.fillStyle = pColor;
        brctx.fill();
      }

      // 5. DIAFRAGMA ANATÓMICO
      const diaYBase = cy + 125;
      const diaDescent = breathExpansion * 48;
      const diaArchHeight = 44 * (1.0 - breathExpansion);

      brctx.beginPath();
      brctx.moveTo(cx - 180 - ribsExpansion * 0.5, diaYBase + diaDescent);
      brctx.bezierCurveTo(
        cx - 85, diaYBase + diaDescent - diaArchHeight,
        cx + 85, diaYBase + diaDescent - diaArchHeight,
        cx + 180 + ribsExpansion * 0.5, diaYBase + diaDescent
      );
      brctx.bezierCurveTo(
        cx + 85, diaYBase + diaDescent - diaArchHeight + 18,
        cx - 85, diaYBase + diaDescent - diaArchHeight + 18,
        cx - 180 - ribsExpansion * 0.5, diaYBase + diaDescent + 18
      );
      brctx.closePath();

      const diaGrad = brctx.createLinearGradient(0, diaYBase + diaDescent - diaArchHeight, 0, diaYBase + diaDescent + 18);
      diaGrad.addColorStop(0, `rgba(217, 119, 6, ${0.32 + breathExpansion * 0.25})`);
      diaGrad.addColorStop(1, "rgba(180, 83, 9, 0.15)");
      brctx.fillStyle = diaGrad;
      brctx.fill();

      brctx.strokeStyle = `rgba(217, 119, 6, ${0.75 + breathExpansion * 0.25})`;
      brctx.lineWidth = 2.6;
      brctx.stroke();

      brctx.fillStyle = "rgba(217, 119, 6, 0.95)";
      brctx.font = "800 11px monospace";
      brctx.textAlign = "center";
      const diaStateStr = (breathPhase === "inhale")
        ? "DIAFRAGMA • [CONTRACCIÓN DESCENDENTE • SUCCIÓN DE AIRE]"
        : (breathPhase === "hold")
        ? "DIAFRAGMA • [APNEA 7s • RETENCIÓN INMÓVIL EN VOLUMEN MÁXIMO]"
        : "DIAFRAGMA • [RELAJACIÓN ASCENDENTE • EXPULSIÓN DE AIRE]";
      brctx.fillText(diaStateStr, cx, diaYBase + diaDescent + 38);

      requestAnimationFrame(renderHolographicLungs);
    }

    function updateBreathHUD() {
      if (isBreathingIntro) return;
      if (!isBreathingActive && breathPhase === "completed") return;

      const badge = document.getElementById("resp-badge-tag");
      if (badge && isBreathingActive) {
        badge.textContent = `DESCOMPRESIÓN NEURAL • CICLO ${breathCycleCount} DE 3`;
      }

      const titleEl = document.getElementById("breath-phase-title");
      const countEl = document.getElementById("breath-num-countdown");
      const instEl = document.getElementById("breath-inst-text");
      const mechEl = document.getElementById("resp-mechanics-detail");

      if (titleEl) {
        if (breathPhase === "inhale") {
          titleEl.textContent = `INHALA • CICLO ${breathCycleCount}/3`;
          titleEl.style.color = "var(--cyan-brand)";
        } else if (breathPhase === "hold") {
          titleEl.textContent = `RETÉN • CICLO ${breathCycleCount}/3`;
          titleEl.style.color = "var(--emerald-safe)";
        } else {
          titleEl.textContent = `EXHALA • CICLO ${breathCycleCount}/3`;
          titleEl.style.color = "var(--indigo-brand)";
        }
      }

      if (countEl) {
        countEl.textContent = breathCountdown;
        if (breathPhase === "inhale") countEl.style.color = "var(--cyan-brand)";
        else if (breathPhase === "hold") countEl.style.color = "var(--emerald-safe)";
        else countEl.style.color = "var(--indigo-brand)";
      }

      if (instEl && mechEl) {
        if (breathPhase === "inhale") {
          instEl.textContent = `Inhala lentamente por la nariz durante 4 segundos expandiendo el abdomen (Ciclo ${breathCycleCount} de 3).`;
          mechEl.textContent = "El diafragma desciende contrayéndose, expande la caja torácica y genera presión negativa que atrae oxígeno profundo.";
        } else if (breathPhase === "hold") {
          instEl.textContent = `Mantén el aire con calma durante 7 segundos exactos en apnea total (Ciclo ${breathCycleCount} de 3).`;
          mechEl.textContent = "La retención satura la hemoglobina y permite el intercambio alveolar completo sin fatiga respiratoria.";
        } else {
          instEl.textContent = `Exhala lentamente por la boca durante 8 segundos vaciando todo el volumen (Ciclo ${breathCycleCount} de 3).`;
          mechEl.textContent = "La exhalación prolongada estimula los barorreceptores arteriales y activa el tono parasimpático que desacelera el ritmo cardíaco.";
        }
      }
    }

    function setBreathingIntroState(autoStart = true) {
      isBreathingIntro = true;
      isBreathingActive = false;
      breathCycleCount = 1;
      breathTimeInCycle = 0;
      prevBreathPhase = "intro";
      breathPhase = "intro";

      const badge = document.getElementById("resp-badge-tag");
      const title = document.getElementById("breath-phase-title");
      const num = document.getElementById("breath-num-countdown");
      const inst = document.getElementById("breath-inst-text");
      const mech = document.getElementById("resp-mechanics-detail");
      const labelToggle = document.getElementById("label-toggle-breath");

      if (badge) badge.textContent = "DESCOMPRESIÓN NEURAL • MÉTODO 4-7-8 (3 CICLOS)";
      if (title) { title.textContent = "Técnica Diafragmática"; title.style.color = "var(--cyan-brand)"; }
      if (num) {
        num.innerHTML = '<div class="resp-cycle-pills-row"><span class="rc-pill">Inhala 4s</span> <span class="rc-arrow">→</span> <span class="rc-pill">Retén 7s</span> <span class="rc-arrow">→</span> <span class="rc-pill">Exhala 8s</span></div>';
      }
      if (inst) inst.textContent = "Esta técnica de respiración 4-7-8 calma el cerebro y estimula directamente el nervio vago. Realizaremos 3 ciclos continuos de descompresión para desacelerar el pulso y estabilizar tu neurobiología antes del simulador vial.";
      if (mech) mech.textContent = "Efecto neurobiológico comprobado: desactiva la hiperalerta del turno laboral y prepara el organismo para un descanso continuo y reparador.";
      if (labelToggle) labelToggle.textContent = "Comenzar Ejercicio Guiado";

      const introKey = autoStart ? "resp_intro_auto" : "resp_intro";
      const introText = autoStart
        ? "Con la técnica de respiración cuatro, siete, ocho logramos calmar el cerebro y regular el ritmo cardíaco, estimulando el nervio vago para inducir el descanso. Iniciamos los tres ciclos guiados."
        : "Con la técnica cuatro, siete, ocho calmamos el cerebro y desaceleramos el pulso cardíaco mediante el nervio vago. Pulsa Comenzar Ejercicio Guiado para iniciar.";

      playSalomeAudio(introKey, introText, () => {
        if (autoStart && currentStageIndex === 1 && !isBreathingActive) {
          breathingAutoStartTimer = setTimeout(() => {
            if (currentStageIndex === 1 && !isBreathingActive) {
              startBreathingActiveCycle();
            }
          }, 600);
        }
      });
    }

    function triggerBreathingVocalCue(phase) {
      if (!isBreathingActive || currentStageIndex !== 1) return;
      if (phase === "inhale") {
        const cycle = Math.min(breathCycleCount, 3);
        const audioKey = "resp_inhale_" + cycle;
        const text = (cycle === 1) ? "Inhala profundamente por la nariz: uno, dos, tres, cuatro."
                   : (cycle === 2) ? "Ciclo dos. Inhala despacio por la nariz: uno, dos, tres, cuatro."
                   : "Ciclo tres. Inhala con calma por la nariz: uno, dos, tres, cuatro.";
        playSalomeAudio(audioKey, text);
      } else if (phase === "hold") {
        playSalomeAudio("resp_hold", "Retén el aire con calma: mantén el diafragma inmóvil durante siete segundos.");
      } else if (phase === "exhale") {
        playSalomeAudio("resp_exhale", "Exhala lentamente por la boca vaciando los pulmones y liberando la tensión.");
      }
    }

    function finishBreathingAndTransitionToSimulator() {
      isBreathingActive = false;
      breathPhase = "completed";

      const badge = document.getElementById("resp-badge-tag");
      const title = document.getElementById("breath-phase-title");
      const num = document.getElementById("breath-num-countdown");
      const inst = document.getElementById("breath-inst-text");
      const mech = document.getElementById("resp-mechanics-detail");
      const labelToggle = document.getElementById("label-toggle-breath");

      if (badge) badge.textContent = "DESCOMPRESIÓN NEURAL • 3 CICLOS COMPLETADOS ✔";
      if (title) {
        title.textContent = "CICLO 3 DE 3 FINALIZADO";
        title.style.color = "var(--emerald-safe)";
      }
      if (num) {
        num.innerHTML = '<span style="color: var(--emerald-safe); font-size: 2.2rem; font-weight: 800;">3 / 3 ✔</span>';
      }
      if (inst) {
        inst.textContent = "¡Excelente descompresión diafragmática! Has completado los tres ciclos del protocolo 4-7-8 con éxito. Tu ritmo cardíaco se ha estabilizado. Pasando automáticamente al simulador vial...";
      }
      if (mech) {
        mech.textContent = "El nervio vago ha restaurado el balance autonómico. Evaluemos ahora tus reflejos y alerta en la autopista.";
      }
      if (labelToggle) {
        labelToggle.textContent = "Iniciando Simulador Vial...";
      }

      const transText = "¡Excelente descompresión diafragmática! Has completado tres ciclos del protocolo cuatro, siete, ocho. Tu ritmo cardíaco se ha estabilizado. Pasamos ahora al simulador de conducción para evaluar tus reflejos en carretera.";

      playSalomeAudio("resp_to_sim_trans", transText, () => {
        if (currentStageIndex === 1) {
          breathingTransitionTimer = setTimeout(() => {
            if (currentStageIndex === 1) {
              goToStage(2);
            }
          }, 700);
        }
      });
    }

    function startBreathingActiveCycle() {
      isBreathingIntro = false;
      isBreathingActive = true;
      breathCycleCount = 1;
      breathTimeInCycle = 0;
      prevBreathPhase = "inhale";
      breathPhase = "inhale";
      lastBreathTimestamp = performance.now();
      const labelToggle = document.getElementById("label-toggle-breath");
      if (labelToggle) labelToggle.textContent = "Pausar Ejercicio";
      playInhaleSound();
      triggerBreathingVocalCue("inhale");
    }

    function toggleBreathingCycle() {
      if (isBreathingIntro) {
        startBreathingActiveCycle();
        return;
      }
      if (breathPhase === "completed") {
        startBreathingActiveCycle();
        return;
      }
      isBreathingActive = !isBreathingActive;
      const toggleLabel = document.getElementById("label-toggle-breath");
      if (toggleLabel) {
        toggleLabel.textContent = isBreathingActive ? "Pausar Ejercicio" : "Reanudar Ejercicio 4-7-8";
      }
      if (isBreathingActive) {
        lastBreathTimestamp = performance.now();
        triggerBreathingVocalCue(breathPhase);
      } else {
        stopAllSomniAudio();
      }
    }

    document.getElementById("btn-toggle-breath-play").addEventListener("click", toggleBreathingCycle);
    document.getElementById("btn-next-to-truck").addEventListener("click", () => goToStage(2));

    /* =========================================================================
       5. FASE 3: SIMULADOR VIAL POV PROCEDURAL Y REALISTA (ANIMACIÓN ACTIVA)
       ========================================================================= */
    const truckFullCanvas = document.getElementById("truck-full-canvas");
    const tfctx = truckFullCanvas.getContext("2d");

    let isDrivingFull = true;
    let truckSpeedFull = 80;
    let truckLanePos = 0.0;    // -1.0 a +1.0
    let truckSteerAngle = 0.0; // Ángulo del volante en radianes
    let fatiguePctFull = 0;
    let hasCrashedFull = false;
    let roadStripeFull = 0;
    let roadCurveFull = 0;

    // Tráfico procedural adelante en la autopista
    let trafficCars = [
      { lane: -0.42, z: 220, speed: 64, color: "#0284c7", isTruck: false },
      { lane: 0.38, z: 380, speed: 70, color: "#dc2626", isTruck: true },
      { lane: -0.25, z: 490, speed: 60, color: "#d97706", isTruck: false }
    ];

    const btnDriveAccelFull = document.getElementById("btn-drive-accel-full");
    const labelAccelFull = document.getElementById("label-accel-full");
    const tfFill = document.getElementById("truck-fatigue-fill-full");
    const tfPctTag = document.getElementById("truck-fatigue-pct-full");
    const truckEyeliTop = document.getElementById("truck-eyelid-top");
    const truckEyeliBottom = document.getElementById("truck-eyelid-bottom");
    const truckBlackoutFull = document.getElementById("truck-blackout-full");
    const truckCrashFull = document.getElementById("truck-crash-full");

    function renderProceduralHighwaySimulator(now) {
      if (!truckFullCanvas || !tfctx) return;
      if (truckFullCanvas.width < 100 || truckFullCanvas.height < 100) {
        const p = truckFullCanvas.parentElement;
        truckFullCanvas.width = (p && p.clientWidth > 50) ? p.clientWidth : (window.innerWidth - 48);
        truckFullCanvas.height = (p && p.clientHeight > 50) ? p.clientHeight : (window.innerHeight - 170);
      }
      const w = truckFullCanvas.width;
      const h = truckFullCanvas.height;
      tfctx.clearRect(0, 0, w, h);

      // 1. Dinámica de avance
      if (isDrivingFull && !hasCrashedFull) {
        roadStripeFull = (roadStripeFull + truckSpeedFull * 0.18) % 40;
        // Curvatura suave de carretera
        roadCurveFull = Math.sin(now * 0.0006) * 45;

        // Actualizar tráfico
        for (let i = 0; i < trafficCars.length; i++) {
          const car = trafficCars[i];
          car.z -= (truckSpeedFull - car.speed) * 0.08;
          if (car.z < 95) car.z = 580;
          if (car.z > 600) car.z = 110;
        }
      }

      // Amortiguación suave del volante hacia el centro
      truckSteerAngle *= 0.93;

      // Vibración de suspensión por rodadura a 80 km/h
      const roadJitter = (isDrivingFull && !hasCrashedFull) ? Math.sin(now * 0.04) * 1.5 : 0;

      // 2. CIELO Y HORIZONTE CREPUSCULAR EXTERIOR
      const horizonY = h * 0.38 + roadJitter;
      const dashY = h * 0.60 + roadJitter;

      const skyGrad = tfctx.createLinearGradient(0, 0, 0, horizonY);
      skyGrad.addColorStop(0, "#020617");
      skyGrad.addColorStop(0.7, "#0f172a");
      skyGrad.addColorStop(1, "#1e293b");
      tfctx.fillStyle = skyGrad;
      tfctx.fillRect(0, 0, w, horizonY);

      // Estrellas y siluetas montañosas lejanas
      tfctx.fillStyle = "rgba(255, 255, 255, 0.45)";
      for (let s = 1; s <= 16; s++) {
        const sx = (s * 105 + now * 0.001) % w;
        const sy = (s * 23) % (horizonY * 0.65);
        tfctx.fillRect(sx, sy, 1.5, 1.5);
      }

      // Montañas en el horizonte
      tfctx.fillStyle = "#090d16";
      tfctx.beginPath();
      tfctx.moveTo(0, horizonY);
      for (let mx = 0; mx <= w; mx += 80) {
        const my = horizonY - 14 - Math.sin(mx * 0.015) * 16;
        tfctx.lineTo(mx, my);
      }
      tfctx.lineTo(w, horizonY);
      tfctx.closePath();
      tfctx.fill();

      // Terreno exterior y bermas
      tfctx.fillStyle = "#05130b";
      tfctx.fillRect(0, horizonY, w, h - horizonY);

      // 3. AUTOPISTA EN PERSPECTIVA 3D CON LÍNEAS REALISTAS
      const roadCenterX = w / 2 - (truckLanePos * 260) + roadCurveFull;
      const horizonRoadW = 90;
      const bottomRoadW = w * 1.05;

      // Asfalto
      const asphaltGrad = tfctx.createLinearGradient(0, horizonY, 0, h);
      asphaltGrad.addColorStop(0, "#1e293b");
      asphaltGrad.addColorStop(1, "#0f172a");
      tfctx.fillStyle = asphaltGrad;

      tfctx.beginPath();
      tfctx.moveTo(roadCenterX - horizonRoadW / 2, horizonY);
      tfctx.lineTo(roadCenterX + horizonRoadW / 2, horizonY);
      tfctx.lineTo(roadCenterX + bottomRoadW / 2, h);
      tfctx.lineTo(roadCenterX - bottomRoadW / 2, h);
      tfctx.closePath();
      tfctx.fill();

      // Conos de luz de los faros sobre el pavimento
      const headLightGrad = tfctx.createRadialGradient(w / 2, h * 0.58, 20, w / 2, h * 0.58, w * 0.45);
      headLightGrad.addColorStop(0, "rgba(254, 240, 138, 0.16)");
      headLightGrad.addColorStop(1, "rgba(254, 240, 138, 0)");
      tfctx.fillStyle = headLightGrad;
      tfctx.fillRect(0, horizonY, w, h - horizonY);

      // Bermas y guardarraíles metálicos
      tfctx.strokeStyle = "#475569";
      tfctx.lineWidth = 3.5;
      tfctx.beginPath();
      tfctx.moveTo(roadCenterX - horizonRoadW / 2, horizonY);
      tfctx.lineTo(roadCenterX - bottomRoadW / 2, h);
      tfctx.moveTo(roadCenterX + horizonRoadW / 2, horizonY);
      tfctx.lineTo(roadCenterX + bottomRoadW / 2, h);
      tfctx.stroke();

      // Líneas continuas laterales reflectivas
      tfctx.strokeStyle = "#FFFFFF";
      tfctx.lineWidth = 4.0;
      tfctx.beginPath();
      tfctx.moveTo(roadCenterX - horizonRoadW * 0.42, horizonY);
      tfctx.lineTo(roadCenterX - bottomRoadW * 0.42, h);
      tfctx.moveTo(roadCenterX + horizonRoadW * 0.42, horizonY);
      tfctx.lineTo(roadCenterX + bottomRoadW * 0.42, h);
      tfctx.stroke();

      // Línea central divisoria discontinua con animación de avance
      tfctx.strokeStyle = "#eab308";
      tfctx.lineWidth = 5.0;
      tfctx.setLineDash([26, 18]);
      tfctx.lineDashOffset = -roadStripeFull;
      tfctx.beginPath();
      tfctx.moveTo(roadCenterX, horizonY);
      tfctx.lineTo(roadCenterX, h);
      tfctx.stroke();
      tfctx.setLineDash([]);

      // Ojos de gato reflectivos que pasan
      tfctx.fillStyle = "rgba(254, 240, 138, 0.85)";
      for (let catY = horizonY + 15; catY < h * 0.72; catY += 35) {
        const t = (catY - horizonY) / (h * 0.72 - horizonY);
        const catX = roadCenterX + (bottomRoadW * 0.42 - horizonRoadW * 0.42) * t;
        tfctx.fillRect(catX - 2, catY, 4, 3);
      }

      // 4. VEHÍCULOS ADELANTE EN LA AUTOPISTA (PERSPECTIVA REALISTA)
      const roadVisH = (dashY - 14) - horizonY;
      for (let i = 0; i < trafficCars.length; i++) {
        const car = trafficCars[i];
        const normDist = Math.max(0, Math.min(1.0, (car.z - 60) / 520));
        const pFactor = 1.0 - Math.pow(normDist, 0.65);
        const carY = horizonY + roadVisH * pFactor;
        const carScale = 0.25 + 0.85 * pFactor;
        const laneSpread = (horizonRoadW * 0.38) + (bottomRoadW * 0.42 - horizonRoadW * 0.38) * pFactor;
        const carX = roadCenterX + car.lane * laneSpread;
        const carW = (car.isTruck ? 84 : 62) * carScale;
        const carH = (car.isTruck ? 68 : 40) * carScale;

        if (carY >= horizonY && carY <= dashY - 4) {
          const carAlpha = Math.min(1.0, (car.z - 95) / 50);
          tfctx.globalAlpha = Math.max(0.1, Math.min(1.0, carAlpha));

          // Sombra
          tfctx.fillStyle = "rgba(0,0,0,0.55)";
          tfctx.fillRect(carX - carW / 2, carY + carH - 4, carW, 8 * carScale);

          // Carrocería
          tfctx.fillStyle = car.color;
          tfctx.fillRect(carX - carW / 2, carY, carW, carH);

          // Techo / cabina
          tfctx.fillStyle = "#0f172a";
          tfctx.fillRect(carX - carW * 0.40, carY + 3 * carScale, carW * 0.80, carH * 0.38);

          // Luces traseras rojas encendidas intensas
          tfctx.fillStyle = "#ef4444";
          tfctx.fillRect(carX - carW * 0.46, carY + carH * 0.58, carW * 0.26, carH * 0.28);
          tfctx.fillRect(carX + carW * 0.20, carY + carH * 0.58, carW * 0.26, carH * 0.28);

          // Resplandor de luces
          tfctx.fillStyle = "rgba(239, 68, 68, 0.4)";
          tfctx.beginPath();
          tfctx.arc(carX - carW * 0.33, carY + carH * 0.72, 8 * carScale, 0, Math.PI * 2);
          tfctx.arc(carX + carW * 0.33, carY + carH * 0.72, 8 * carScale, 0, Math.PI * 2);
          tfctx.fill();

          // Matrícula reflectiva
          tfctx.fillStyle = "#f8fafc";
          tfctx.fillRect(carX - carW * 0.16, carY + carH * 0.68, carW * 0.32, carH * 0.20);

          tfctx.globalAlpha = 1.0;
        }
      }

      // 5. CABINA EN PRIMERA PERSONA (POV DEL CONDUCTOR REALISTA)
      const pilarW = Math.max(40, w * 0.055);

      // Pilares A izquierdo y derecho
      tfctx.fillStyle = "#090d16";
      tfctx.beginPath();
      tfctx.moveTo(0, 0);
      tfctx.lineTo(pilarW, 0);
      tfctx.lineTo(pilarW * 1.6, h * 0.66);
      tfctx.lineTo(0, h * 0.66);
      tfctx.closePath();
      tfctx.fill();

      tfctx.beginPath();
      tfctx.moveTo(w, 0);
      tfctx.lineTo(w - pilarW, 0);
      tfctx.lineTo(w - pilarW * 1.6, h * 0.66);
      tfctx.lineTo(w, h * 0.66);
      tfctx.closePath();
      tfctx.fill();

      // Espejo retrovisor central (Refleja la vía que dejamos atrás)
      tfctx.fillStyle = "#090d16";
      tfctx.fillRect(w / 2 - 80, 24, 160, 48);
      tfctx.strokeStyle = "#334155";
      tfctx.lineWidth = 3;
      tfctx.strokeRect(w / 2 - 80, 24, 160, 48);

      // Reflejo en el espejo
      const mirrorGrad = tfctx.createLinearGradient(0, 26, 0, 70);
      mirrorGrad.addColorStop(0, "#0f172a");
      mirrorGrad.addColorStop(1, "#1e293b");
      tfctx.fillStyle = mirrorGrad;
      tfctx.fillRect(w / 2 - 77, 27, 154, 42);

      // Faros en retrovisor
      tfctx.fillStyle = "rgba(254, 240, 138, 0.75)";
      tfctx.beginPath();
      tfctx.arc(w / 2 - 25, 48, 4, 0, Math.PI * 2);
      tfctx.arc(w / 2 + 25, 48, 4, 0, Math.PI * 2);
      tfctx.fill();

      // Retrovisor lateral izquierdo
      tfctx.fillStyle = "#090d16";
      tfctx.fillRect(pilarW + 8, h * 0.28, 46, 80);
      tfctx.strokeStyle = "#475569";
      tfctx.lineWidth = 2;
      tfctx.strokeRect(pilarW + 8, h * 0.28, 46, 80);

      // TABLERO DE MANDOS (DASHBOARD REALISTA)
      tfctx.fillStyle = "#090d16";
      tfctx.beginPath();
      tfctx.moveTo(0, dashY);
      tfctx.quadraticCurveTo(w / 2, dashY - 18, w, dashY);
      tfctx.lineTo(w, h);
      tfctx.lineTo(0, h);
      tfctx.closePath();
      tfctx.fill();

      // Costura / iluminación ambiental cian en la consola
      tfctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      tfctx.lineWidth = 2.5;
      tfctx.beginPath();
      tfctx.moveTo(0, dashY);
      tfctx.quadraticCurveTo(w / 2, dashY - 18, w, dashY);
      tfctx.stroke();

      // CUADRO DE INSTRUMENTOS ANALÓGICO E ILUMINADO (VELOCÍMETRO Y TACÓMETRO)
      const clusterX = w * 0.38;
      const clusterY = h * 0.69;

      // Reloj 1: Tacómetro (RPM)
      drawAnalogDial(tfctx, clusterX - 85, clusterY, 46, "RPM x1000", isDrivingFull ? 2.4 : 0.8, 6.0, "#38bdf8");

      // Reloj 2: Velocímetro (KM/H)
      const speedDialColor = (fatiguePctFull > 40 || truckSpeedFull > 95) ? "#ef4444" : "#10b981";
      drawAnalogDial(tfctx, clusterX + 85, clusterY, 54, "KM/H", truckSpeedFull, 160, speedDialColor);

      // Pantalla central digital del cuadro
      tfctx.fillStyle = "#030712";
      tfctx.fillRect(clusterX - 26, clusterY - 36, 52, 54);
      tfctx.strokeStyle = "#1e293b";
      tfctx.lineWidth = 1.5;
      tfctx.strokeRect(clusterX - 26, clusterY - 36, 52, 54);

      tfctx.fillStyle = "#38bdf8";
      tfctx.font = "800 12px monospace";
      tfctx.textAlign = "center";
      tfctx.fillText("D4", clusterX, clusterY - 16);
      tfctx.fillStyle = "#FFFFFF";
      tfctx.font = "800 14px monospace";
      tfctx.fillText(truckSpeedFull, clusterX, clusterY + 2);
      tfctx.font = "700 8px monospace";
      tfctx.fillStyle = fatiguePctFull > 40 ? "#ef4444" : "#10b981";
      tfctx.fillText(fatiguePctFull > 40 ? "! ALERTA !" : "LANE OK", clusterX, clusterY + 14);

      // Brazos/mangas del conductor en perspectiva hacia el volante
      tfctx.fillStyle = "#0f172a";
      tfctx.beginPath();
      tfctx.moveTo(w * 0.08, h);
      tfctx.lineTo(clusterX - 130, h * 0.80);
      tfctx.lineTo(clusterX - 95, h * 0.80);
      tfctx.lineTo(w * 0.22, h);
      tfctx.closePath();
      tfctx.fill();

      tfctx.beginPath();
      tfctx.moveTo(w * 0.54, h);
      tfctx.lineTo(clusterX + 95, h * 0.80);
      tfctx.lineTo(clusterX + 130, h * 0.80);
      tfctx.lineTo(w * 0.68, h);
      tfctx.closePath();
      tfctx.fill();

      // VOLANTE DE CUERO TEXTURIZADO CON ROTACIÓN DINÁMICA
      const wheelCX = clusterX;
      const wheelCY = h * 0.79;
      const wheelR = Math.min(145, w * 0.16);

      tfctx.save();
      tfctx.translate(wheelCX, wheelCY);
      tfctx.rotate(truckSteerAngle);

      // Aro exterior del volante (cuero negro con textura)
      tfctx.strokeStyle = "#172033";
      tfctx.lineWidth = 24;
      tfctx.beginPath();
      tfctx.arc(0, 0, wheelR, 0, Math.PI * 2);
      tfctx.stroke();

      // Costura interior
      tfctx.strokeStyle = "#38bdf8";
      tfctx.lineWidth = 2.0;
      tfctx.setLineDash([4, 4]);
      tfctx.beginPath();
      tfctx.arc(0, 0, wheelR - 10, 0, Math.PI * 2);
      tfctx.stroke();
      tfctx.setLineDash([]);

      // Radios del volante
      tfctx.fillStyle = "#0f172a";
      tfctx.fillRect(-wheelR + 10, -12, wheelR * 0.65, 24);
      tfctx.fillRect(wheelR * 0.35 - 10, -12, wheelR * 0.65, 24);
      tfctx.fillRect(-18, 0, 36, wheelR * 0.85);

      // Centro del volante / Airbag con logo
      tfctx.beginPath();
      tfctx.arc(0, 0, 46, 0, Math.PI * 2);
      tfctx.fillStyle = "#090d16";
      tfctx.fill();
      tfctx.strokeStyle = "#475569";
      tfctx.lineWidth = 3;
      tfctx.stroke();

      tfctx.fillStyle = "#f8fafc";
      tfctx.font = "800 10px monospace";
      tfctx.fillText("SST DRIVE", 0, 4);

      // Guantes ergonómicos del conductor sujetando el volante
      tfctx.fillStyle = "#1e293b";
      tfctx.beginPath();
      tfctx.arc(-wheelR, 0, 18, 0, Math.PI * 2);
      tfctx.fill();
      tfctx.strokeStyle = "#38bdf8";
      tfctx.lineWidth = 2;
      tfctx.stroke();
      tfctx.fillStyle = "#0f172a";
      tfctx.fillRect(-wheelR - 8, -12, 16, 24);

      tfctx.fillStyle = "#1e293b";
      tfctx.beginPath();
      tfctx.arc(wheelR, 0, 18, 0, Math.PI * 2);
      tfctx.fill();
      tfctx.strokeStyle = "#38bdf8";
      tfctx.lineWidth = 2;
      tfctx.stroke();
      tfctx.fillStyle = "#0f172a";
      tfctx.fillRect(wheelR - 8, -12, 16, 24);

      tfctx.restore();

      requestAnimationFrame(renderProceduralHighwaySimulator);
    }

    // Dibuja un reloj analógico de instrumentación
    function drawAnalogDial(ctx, x, y, radius, label, value, maxVal, color) {
      ctx.beginPath();
      ctx.arc(x, y, radius, 0, Math.PI * 2);
      ctx.fillStyle = "#030712";
      ctx.fill();
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // Marcas de graduación
      ctx.strokeStyle = "rgba(255, 255, 255, 0.4)";
      ctx.lineWidth = 1.5;
      for (let a = -Math.PI * 0.75; a <= Math.PI * 0.75; a += Math.PI * 0.25) {
        ctx.beginPath();
        ctx.moveTo(x + Math.cos(a) * (radius - 8), y + Math.sin(a) * (radius - 8));
        ctx.lineTo(x + Math.cos(a) * (radius - 2), y + Math.sin(a) * (radius - 2));
        ctx.stroke();
      }

      // Aguja indicadora con rotación analógica
      const pct = Math.min(1.0, value / maxVal);
      const needleAng = -Math.PI * 0.75 + pct * (Math.PI * 1.5);

      ctx.strokeStyle = color;
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x + Math.cos(needleAng) * (radius - 6), y + Math.sin(needleAng) * (radius - 6));
      ctx.stroke();

      // Centro de aguja
      ctx.beginPath();
      ctx.arc(x, y, 4, 0, Math.PI * 2);
      ctx.fillStyle = color;
      ctx.fill();

      // Rótulo
      ctx.fillStyle = "#94a3b8";
      ctx.font = "800 8px monospace";
      ctx.textAlign = "center";
      ctx.fillText(label, x, y + radius * 0.55);
    }

    function setSteeringDirect(dir) {
      if (hasCrashedFull) return;
      if (dir === "left") {
        truckSteerAngle = -0.55;
        truckLanePos = Math.max(-1.0, truckLanePos - 0.22);
      } else if (dir === "right") {
        truckSteerAngle = 0.55;
        truckLanePos = Math.min(1.0, truckLanePos + 0.22);
      }
    }

    document.getElementById("btn-steer-left-full").addEventListener("click", () => setSteeringDirect("left"));
    document.getElementById("btn-steer-right-full").addEventListener("click", () => setSteeringDirect("right"));

    window.addEventListener("keydown", (e) => {
      if (currentStageIndex !== 2) return;
      if (e.key === "ArrowLeft" || e.key.toLowerCase() === "a") setSteeringDirect("left");
      if (e.key === "ArrowRight" || e.key.toLowerCase() === "d") setSteeringDirect("right");
    });

    btnDriveAccelFull.addEventListener("click", () => {
      isDrivingFull = !isDrivingFull;
      truckSpeedFull = isDrivingFull ? 80 : 0;
      labelAccelFull.textContent = isDrivingFull ? "Frenar / Detener" : "Acelerar a 80 km/h";
    });

    document.getElementById("btn-trigger-microsleep-full").addEventListener("click", triggerFullMicrosleep);

    let fatigueTimer = null;
    let crashTransTimer = null;

    function triggerFullMicrosleep() {
      if (hasCrashedFull || currentStageIndex !== 2) return;
      speakSomniBot("Alerta de fatiga crítica: la acumulación de adenosina vence el control consciente. Los párpados caen en microsueño.", null, "sim_alert");

      let currentF = 0;
      if (fatigueTimer) clearInterval(fatigueTimer);
      fatigueTimer = setInterval(() => {
        if (currentStageIndex !== 2) {
          clearInterval(fatigueTimer);
          fatigueTimer = null;
          return;
        }
        // Progresión gradual a lo largo de ~7.2 segundos para permitir que la locución termine de forma natural
        currentF += 2.5;
        if (currentF > 100) currentF = 100;
        fatiguePctFull = currentF;

        if (tfFill) tfFill.style.width = currentF + "%";
        if (tfPctTag) {
          tfPctTag.textContent = Math.round(currentF) + "% (" + (currentF < 40 ? "ALERTA" : currentF < 75 ? "PESADEZ" : "PELIGRO") + ")";
          tfPctTag.style.color = currentF < 40 ? "var(--emerald-safe)" : currentF < 75 ? "var(--amber-alert)" : "var(--red-alert)";
        }

        // Párpados caen progresivamente
        const eyelidH = currentF * 0.48;
        if (truckEyeliTop) truckEyeliTop.style.height = eyelidH + "%";
        if (truckEyeliBottom) truckEyeliBottom.style.height = eyelidH + "%";

        // Desviación involuntaria del carril
        truckLanePos += (Math.random() - 0.45) * 0.12;

        if (currentF >= 100) {
          clearInterval(fatigueTimer);
          fatigueTimer = null;
          if (currentStageIndex === 2) {
            executeBlackoutAndCrash();
          }
        }
      }, 180);
    }

    function executeBlackoutAndCrash() {
      if (truckBlackoutFull) truckBlackoutFull.classList.add("is-active");
      speakSomniBot("Microsueño total. Has perdido el control durante 3 segundos a 80 kilómetros por hora.", null, "sim_crash");

      setTimeout(() => {
        if (truckBlackoutFull) truckBlackoutFull.classList.remove("is-active");
        hasCrashedFull = true;
        isDrivingFull = false;

        playScreechAndCrashSound();
        if (truckCrashFull) {
          truckCrashFull.classList.add("is-active");

          const autoNextTag = document.getElementById("truck-auto-next-tag");
          let countSec = 8;
          if (autoNextTag) autoNextTag.textContent = `Avanzando a Decisiones de Turno en ${countSec}s...`;

          if (crashTransTimer) clearInterval(crashTransTimer);
          crashTransTimer = setInterval(() => {
            if (currentStageIndex !== 2 || !hasCrashedFull) {
              clearInterval(crashTransTimer);
              crashTransTimer = null;
              return;
            }
            countSec--;
            if (autoNextTag) autoNextTag.textContent = `Avanzando a Decisiones de Turno en ${countSec}s...`;
            if (countSec <= 0) {
              clearInterval(crashTransTimer);
              crashTransTimer = null;
              if (currentStageIndex === 2 && hasCrashedFull) {
                goToStage(3);
              }
            }
          }, 1000);
        }
      }, 2800);
    }

    let drivingAutoTimer = null;
    let drivingElapsedSec = 0;

    function startDrivingSimulatorStage() {
      resizeAllCanvases();
      hasCrashedFull = false;
      isDrivingFull = true;
      truckSpeedFull = 80;
      truckLanePos = 0;
      fatiguePctFull = 0;
      drivingElapsedSec = 0;

      if (truckCrashFull) truckCrashFull.classList.remove("is-active");
      if (truckBlackoutFull) truckBlackoutFull.classList.remove("is-active");
      if (truckEyeliTop) truckEyeliTop.style.height = "0%";
      if (truckEyeliBottom) truckEyeliBottom.style.height = "0%";
      if (tfFill) tfFill.style.width = "0%";
      if (tfPctTag) { tfPctTag.textContent = "0% (ALERTA)"; tfPctTag.style.color = "var(--emerald-safe)"; }
      labelAccelFull.textContent = "Frenar / Detener";

      speakSomniBot("Estás al volante en la autopista a 80 km/h. Conduce con las teclas A y D o los botones de giro. Mantente atento a los vehículos en la vía... en unos momentos la fatiga acumulada pondrá a prueba tus reflejos.", null, "sim_driving");

      clearInterval(drivingAutoTimer);
      drivingAutoTimer = setInterval(() => {
        if (currentStageIndex !== 2) {
          clearInterval(drivingAutoTimer);
          return;
        }
        if (isDrivingFull && !hasCrashedFull) {
          drivingElapsedSec++;
          // A los 10 segundos continuos al volante se activa automáticamente el microsueño
          if (drivingElapsedSec >= 10) {
            clearInterval(drivingAutoTimer);
            triggerFullMicrosleep();
          }
        }
      }, 1000);
    }

    document.getElementById("btn-restart-driving-full").addEventListener("click", () => {
      startDrivingSimulatorStage();
      speakSomniBot("Simulador reiniciado con reflejos óptimos y descanso pleno. Tienes 10 segundos al volante antes de que la fatiga reaparezca.");
    });

    /* =========================================================================
       6. FASE 4: DECISIONES DE TURNO (DILEMAS)
       ========================================================================= */
    const dilemmaScenarios = [
      {
        category: "DECISIÓN 01 • DESCANSO PREVIO AL TURNO",
        question: "¿Qué haces 45 minutos antes de dormir?",
        context: "La exposición a pantallas inhibe la secreción de melatonina y engaña al cerebro haciéndole creer que es de día.",
        optA: "Revisar celular en la cama con brillo alto",
        optB: "Desconexión digital con luz tenue y respiración 4-7-8",
        goodChoice: "B",
        expA: "OPCIÓN A: La luz azul de 480nm suprime la melatonina en un 88%. El cerebro permanece en ondas Beta altas y no puede entrar en sueño profundo Delta.",
        expB: "OPCIÓN B (CORRECTA): La desconexión y la técnica 4-7-8 activan el sistema parasimpático, induciendo un lavado glinfático completo durante la noche."
      },
      {
        category: "DECISIÓN 02 • GESTIÓN DE ENERGÍA Y FATIGA",
        question: "Sientes pesadez y bostezo a las 3:00 PM durante tu jornada. ¿Qué eliges?",
        context: "El pico de adenosina en la tarde genera presión de sueño natural. La elección determina tu seguridad.",
        optA: "Tomar bebida energizante de alta dosis",
        optB: "Pausa activa con caminata de 10 min e hidratación con agua fresca",
        goodChoice: "B",
        expA: "OPCIÓN A: Los energizantes enmascaran la fatiga bloqueando temporalmente los receptores pero provocan un efecto rebote severo 90 minutos después.",
        expB: "OPCIÓN B (CORRECTA): El movimiento físico y el agua fría activan la circulación periférica y reducen la adenosina sin alterar el descanso nocturno posterior."
      },
      {
        category: "DECISIÓN 03 • DESCOMPRESIÓN MENTAL ANTES DE LA CAMA",
        question: "Llegas a casa con preocupaciones laborales en mente. ¿Cómo las manejas?",
        context: "La rumiación mental activa la amígdala cerebral e impide la relajación cardiovascular necesaria para el sueño.",
        optA: "Acostarte rumiando los pendientes en la almohada",
        optB: "Anotar pendientes en papel para el día siguiente y respirar 4-7-8",
        goodChoice: "B",
        expA: "OPCIÓN A: Llevar pendientes a la cama mantiene elevado el cortisol basal (+140%), impidiendo la desconexión del lóbulo prefrontal.",
        expB: "OPCIÓN B (CORRECTA): Externalizar los pendientes en papel vacía la memoria de trabajo y la técnica 4-7-8 reduce la frecuencia cardíaca a ritmo de reposo."
      }
    ];

    let currentDilemmaIdx = 0;
    const dilCategoryTag = document.getElementById("dil-category-tag");
    const dilQuestionText = document.getElementById("dil-question-text");
    const dilContextText = document.getElementById("dil-context-text");
    const btnDilA = document.getElementById("btn-dil-a");
    const btnDilB = document.getElementById("btn-dil-b");
    const textDilOptA = document.getElementById("text-dil-opt-a");
    const textDilOptB = document.getElementById("text-dil-opt-b");
    const dilExplanationBox = document.getElementById("dil-explanation-box");
    const btnDilNext = document.getElementById("btn-dil-next-scenario");
    const dilemmaBrainCanvas = document.getElementById("dilemma-brain-canvas");
    const dbctx = dilemmaBrainCanvas.getContext("2d");

    let dilemmaBrainState = "calm";

    function renderDilemma(idx, playVoice = false) {
      currentDilemmaIdx = idx;
      const d = dilemmaScenarios[idx];

      dilCategoryTag.textContent = d.category;
      dilQuestionText.textContent = d.question;
      dilContextText.textContent = d.context;
      textDilOptA.textContent = d.optA;
      textDilOptB.textContent = d.optB;

      btnDilA.classList.remove("is-chosen-good", "is-chosen-bad");
      btnDilB.classList.remove("is-chosen-good", "is-chosen-bad");
      btnDilA.disabled = false;
      btnDilB.disabled = false;

      dilExplanationBox.classList.remove("is-active", "good", "bad");
      dilExplanationBox.innerHTML = "";
      btnDilNext.style.display = "none";

      dilemmaBrainState = "calm";
      if (playVoice) {
        speakSomniBot(d.category + ": " + d.question);
      }
    }

    function chooseDilemmaOption(choice) {
      const d = dilemmaScenarios[currentDilemmaIdx];
      btnDilA.disabled = true;
      btnDilB.disabled = true;

      const isGood = (choice === d.goodChoice);
      const chosenBtn = choice === "A" ? btnDilA : btnDilB;
      const otherBtn = choice === "A" ? btnDilB : btnDilA;

      if (isGood) {
        chosenBtn.classList.add("is-chosen-good");
        dilExplanationBox.className = "dilemma-explanation-box is-active good";
        dilExplanationBox.innerHTML = `<strong>Elección Correcta:</strong> ${d.expB}`;
        dilemmaBrainState = "calm";
        speakSomniBot("Excelente decisión. Esta conducta protege tu neurobiología y asegura un descanso reparador.");
      } else {
        chosenBtn.classList.add("is-chosen-bad");
        otherBtn.classList.add("is-chosen-good");
        dilExplanationBox.className = "dilemma-explanation-box is-active bad";
        dilExplanationBox.innerHTML = `<strong>Riesgo Crítico:</strong> ${d.expA}<br><br><strong>Medida Preventiva:</strong> ${d.expB}`;
        dilemmaBrainState = "stress";
        speakSomniBot("Atención: este hábito incrementa la tensión cortical y compromete tu estado de alerta en el turno.");
      }

      btnDilNext.style.display = "inline-flex";
    }

    btnDilA.addEventListener("click", () => chooseDilemmaOption("A"));
    btnDilB.addEventListener("click", () => chooseDilemmaOption("B"));

    btnDilNext.addEventListener("click", () => {
      if (currentDilemmaIdx < dilemmaScenarios.length - 1) {
        renderDilemma(currentDilemmaIdx + 1);
      } else {
        goToStage(4);
      }
    });

    let dilemmaRotY = 0.2;

    function renderDilemmaBrain(now) {
      if (!dilemmaBrainCanvas || !dbctx) return;
      const w = dilemmaBrainCanvas.width;
      const h = dilemmaBrainCanvas.height;
      dbctx.clearRect(0, 0, w, h);

      dilemmaRotY += 0.0035;

      const cx = w / 2;
      const cy = h / 2 - 12;
      const baseScale = Math.min(w, h) * 0.0023;
      const fov = 400;

      const cosY = Math.cos(dilemmaRotY), sinY = Math.sin(dilemmaRotY);
      const pitch = 0.18;
      const cosX = Math.cos(pitch), sinX = Math.sin(pitch);

      const isStress = (dilemmaBrainState === "stress");
      const pulseMultiplier = isStress ? 4.2 : 1.0;

      // Actualizar telemetría de dilemas
      const telState = document.getElementById("dil-telemetry-state");
      const telFreq = document.getElementById("dil-telemetry-freq");
      if (telState && telFreq) {
        if (isStress) {
          telState.textContent = "SOBRECARGA AMIGDALINA";
          telState.style.color = "var(--red-alert)";
          telFreq.textContent = "28.5 Hz (BETA RÁPIDA)";
          telFreq.style.color = "var(--red-alert)";
        } else {
          telState.textContent = "EQUILIBRIO PREFRONTAL";
          telState.style.color = "var(--cyan-brand)";
          telFreq.textContent = "10.2 Hz (ALFA SERENA)";
          telFreq.style.color = "var(--emerald-safe)";
        }
      }

      // Proyectar nodos cerebrales en 3D
      const projected = [];
      for (let i = 0; i < brain3DNodes.length; i++) {
        const n = brain3DNodes[i];
        const pulse = 1.0 + Math.sin(now * n.speed * pulseMultiplier + n.phase) * (isStress ? 0.08 : 0.035);
        let bx = n.baseX * pulse;
        let by = n.baseY * pulse;
        let bz = n.baseZ * pulse;

        const x1 = bx * cosY - bz * sinY;
        const z1 = bx * sinY + bz * cosY;
        const y2 = by * cosX - z1 * sinX;
        const z2 = by * sinX + z1 * cosX;

        const dist = fov / (fov + z2 * baseScale);
        projected.push({
          px: cx + x1 * baseScale * dist,
          py: cy + y2 * baseScale * dist,
          dist,
          radius: n.radius,
          isDeep: n.isDeep
        });
      }

      // Axones en 3D
      dbctx.strokeStyle = isStress ? "rgba(239, 68, 68, 0.20)" : "rgba(2, 132, 199, 0.22)";
      dbctx.lineWidth = isStress ? 1.0 : 0.8;
      dbctx.beginPath();
      for (let i = 0; i < brain3DAxons.length; i += 2) {
        const ax = brain3DAxons[i];
        const p1 = projected[ax.a];
        const p2 = projected[ax.b];
        if (!p1 || !p2) continue;
        dbctx.moveTo(p1.px, p1.py);
        dbctx.lineTo(p2.px, p2.py);
      }
      dbctx.stroke();

      // Nodos en 3D
      for (let i = 0; i < projected.length; i++) {
        const p = projected[i];
        const r = Math.max(1.2, p.radius * p.dist * 0.9);
        dbctx.beginPath();
        dbctx.arc(p.px, p.py, r, 0, Math.PI * 2);
        if (isStress) {
          dbctx.fillStyle = p.isDeep ? "#f59e0b" : "#ef4444";
        } else {
          dbctx.fillStyle = p.isDeep ? "#059669" : "#0284c7";
        }
        dbctx.fill();
      }

      requestAnimationFrame(renderDilemmaBrain);
    }

    /* =========================================================================
       7. FASE 5: FISIOLOGÍA DEL ESTRÉS Y EL SUEÑO • NEUROBIOLOGÍA CLÍNICA
       ========================================================================= */
    function setStressMode(mode, playVoice = true) {
      const isAlert = (mode === "alert");

      const btnAlert = document.getElementById("btn-stress-mode-alert");
      const btnCalm = document.getElementById("btn-stress-mode-calm");
      if (btnAlert) btnAlert.classList.toggle("is-active", isAlert);
      if (btnCalm) btnCalm.classList.toggle("is-active", !isAlert);

      const titleEl = document.getElementById("bio-circuit-mode-title");
      const pillEl = document.getElementById("bio-circuit-status-pill");
      if (titleEl) {
        titleEl.textContent = isAlert 
          ? "DIBUJO ANATÓMICO • SOBRECARGA Y ALERTA SIMPÁTICA" 
          : "DIBUJO ANATÓMICO • DESCOMPRESIÓN Y TONO VAGAL";
      }
      if (pillEl) {
        pillEl.textContent = isAlert ? "Sobrecarga Activa" : "Tono Vagal Activo";
        pillEl.className = "bio-status-pill " + (isAlert ? "alert" : "calm");
      }

      // Actualizar SVG Anatómico
      const svgEl = document.getElementById("bio-anatomy-svg");
      if (svgEl) {
        svgEl.className.baseVal = isAlert ? "bio-svg-alert" : "bio-svg-calm";
      }

      // Amígdala
      const amygdalaGlow = document.getElementById("bio-amygdala-glow");
      const amygdalaCore = document.getElementById("bio-amygdala-core");
      const amygdalaBursts = document.getElementById("bio-amygdala-bursts");
      if (amygdalaGlow) amygdalaGlow.setAttribute("fill", isAlert ? "url(#grad-amygdala-alert)" : "url(#grad-amygdala-calm)");
      if (amygdalaCore) amygdalaCore.setAttribute("fill", isAlert ? "#DC2626" : "#0284C7");
      if (amygdalaBursts) amygdalaBursts.style.display = isAlert ? "block" : "none";

      // Monitor EEG
      const eegPath = document.getElementById("bio-eeg-path");
      const eegText = document.getElementById("bio-eeg-text");
      if (eegPath) {
        if (isAlert) {
          eegPath.setAttribute("d", "M 16,43 L 26,43 L 31,35 L 38,49 L 45,36 L 53,48 L 61,43 L 75,43 L 82,34 L 90,50 L 98,36 L 106,48 L 114,43 L 128,43 L 135,35 L 144,43");
          eegPath.setAttribute("stroke", "#DC2626");
        } else {
          eegPath.setAttribute("d", "M 16,43 Q 32,31 48,43 T 80,43 T 112,43 T 144,43");
          eegPath.setAttribute("stroke", "#059669");
        }
      }
      if (eegText) {
        eegText.textContent = isAlert ? "BETA 28.4 Hz • HIPERALERTA" : "DELTA 2.1 Hz • REPARACIÓN";
        eegText.setAttribute("font-size", "8.4");
        eegText.setAttribute("fill", isAlert ? "#DC2626" : "#059669");
      }

      // Nervio Vago
      const vagusFiber = document.getElementById("bio-vagus-fiber");
      if (vagusFiber) vagusFiber.setAttribute("stroke", isAlert ? "#EF4444" : "#0284C7");
      const vagusNodes = document.querySelectorAll(".bio-vagus-node");
      vagusNodes.forEach(node => {
        node.setAttribute("fill", isAlert ? "#DC2626" : "#0284C7");
      });

      // Lavado Glinfático
      const glymphBg = document.getElementById("bio-glymph-icon-bg");
      const glymphPath = document.getElementById("bio-glymph-icon-path");
      const glymphVal = document.getElementById("bio-glymph-val");
      const glymphSub = document.getElementById("bio-glymph-sub");
      if (glymphBg) glymphBg.setAttribute("fill", isAlert ? "rgba(239, 68, 68, 0.1)" : "rgba(5, 150, 105, 0.1)");
      if (glymphPath) glymphPath.setAttribute("fill", isAlert ? "#DC2626" : "#059669");
      if (glymphVal) {
        glymphVal.textContent = isAlert ? "0% DRENAJE" : "98% LAVADO ACTIVO";
        glymphVal.setAttribute("fill", isAlert ? "#DC2626" : "#059669");
      }
      if (glymphSub) glymphSub.textContent = isAlert ? "Adenosina estancada en corteza" : "Lavado activo de toxinas";
      const glymphBar = document.getElementById("bio-glymph-bar");
      if (glymphBar) {
        glymphBar.setAttribute("width", isAlert ? "8" : "145");
        glymphBar.setAttribute("fill", isAlert ? "#DC2626" : "#059669");
      }
      const hormoneBar = document.getElementById("bio-hormone-bar");
      if (hormoneBar) {
        hormoneBar.setAttribute("width", isAlert ? "140" : "14");
        hormoneBar.setAttribute("fill", isAlert ? "#DC2626" : "#0284C7");
      }

      // Eje Suprarrenal / Hormonas
      const hormoneBg = document.getElementById("bio-hormone-icon-bg");
      const hormonePath = document.getElementById("bio-hormone-icon-path");
      const hormoneVal = document.getElementById("bio-hormone-val");
      const hormoneSub = document.getElementById("bio-hormone-sub");
      if (hormoneBg) hormoneBg.setAttribute("fill", isAlert ? "rgba(239, 68, 68, 0.1)" : "rgba(2, 132, 199, 0.1)");
      if (hormonePath) hormonePath.setAttribute("stroke", isAlert ? "#DC2626" : "#0284C7");
      if (hormoneVal) {
        hormoneVal.textContent = isAlert ? "Cortisol: +180% Sérico" : "Melatonina Óptima (92 pg/mL)";
        hormoneVal.setAttribute("fill", isAlert ? "#DC2626" : "#0284C7");
        hormoneVal.setAttribute("font-size", isAlert ? "11.4" : "10.8");
      }
      if (hormoneSub) hormoneSub.textContent = isAlert ? "Melatonina bloqueada" : "Cortisol suprimido (<6 µg/dL)";

      // Medidor de Conducción Vial
      const dialArc = document.getElementById("bio-dial-arc");
      const dialNeedle = document.getElementById("bio-dial-needle");
      const driveRiskVal = document.getElementById("bio-drive-risk-val");
      const driveRiskLbl = document.getElementById("bio-drive-risk-lbl");
      const driveDescBg = document.getElementById("bio-drive-desc-bg");
      const driveDescTxt = document.getElementById("bio-drive-desc-txt");
      if (dialArc) {
        dialArc.setAttribute("stroke", isAlert ? "#DC2626" : "#059669");
        dialArc.setAttribute("d", isAlert ? "M 20,58 A 16,16 0 1,1 52,58" : "M 20,58 A 16,16 0 0,1 30,43");
      }
      if (dialNeedle) {
        dialNeedle.setAttribute("stroke", isAlert ? "#DC2626" : "#059669");
        if (isAlert) {
          dialNeedle.setAttribute("x2", "48"); dialNeedle.setAttribute("y2", "43");
        } else {
          dialNeedle.setAttribute("x2", "24"); dialNeedle.setAttribute("y2", "43");
        }
      }
      // Actualizar puntos de conexión (leader dots)
      const leadColor = isAlert ? "#DC2626" : "#059669";
      for (let d = 1; d <= 4; d++) {
        const dot = document.getElementById("lead-dot-" + d);
        if (dot) dot.setAttribute("fill", leadColor);
      }
      if (driveRiskVal) {
        driveRiskVal.textContent = isAlert ? "15.0x" : "0.0x";
        driveRiskVal.setAttribute("fill", isAlert ? "#DC2626" : "#059669");
      }
      if (driveRiskLbl) driveRiskLbl.textContent = isAlert ? "Riesgo Microsueño" : "Reflejos al 100%";
      if (driveDescBg) driveDescBg.setAttribute("fill", isAlert ? "rgba(239, 68, 68, 0.08)" : "rgba(5, 150, 105, 0.08)");
      if (driveDescTxt) {
        driveDescTxt.textContent = isAlert ? "Cabeceo 3 a 5s = 67m a ciegas" : "Frenado y reflejos al 100%";
        driveDescTxt.setAttribute("fill", isAlert ? "#DC2626" : "#059669");
      }

      // Pie del dibujo anatómico
      const bafTag = document.getElementById("baf-organ-tag");
      const bafDesc = document.getElementById("baf-organ-desc");
      if (bafTag) bafTag.textContent = isAlert ? "CORTE SAGITAL • HIPERACTIVACIÓN AMIGDALINA" : "CORTE SAGITAL • TONO VAGAL Y REPARACIÓN";
      if (bafDesc) {
        bafDesc.textContent = isAlert 
          ? "La sobrecarga operativa activa la amígdala cerebral, inhibiendo el freno consciente de la corteza prefrontal, disparando el cortisol y bloqueando el lavado glinfático. En ruta, el conductor cabeceará de 3 a 5 segundos de forma involuntaria."
          : "En estado de recuperación y tono vagal, el sistema glinfático drena la adenosina acumulada en la corteza y la melatonina alcanza su pico nocturno. Esto repara las conexiones neuronales y garantiza reflejos del 100% al volante.";
      }

      // COLUMNA DERECHA: TABLERO BIOMÉTRICO
      const scardBadge = document.getElementById("scard-telemetry-badge");
      if (scardBadge) {
        scardBadge.textContent = isAlert ? "MONITOR BIOMÉDICO • COLAPSO POR ESTRÉS" : "MONITOR BIOMÉDICO • EQUILIBRIO NEUROVEGETATIVO";
        scardBadge.className = "scard-header-badge " + (isAlert ? "alert" : "calm");
      }

      const valCortisol = document.getElementById("bm-val-cortisol");
      const barCortisol = document.getElementById("bm-bar-cortisol");
      const subCortisol = document.getElementById("bm-sub-cortisol");
      if (valCortisol) valCortisol.textContent = isAlert ? "28.6 µg/dL" : "6.4 µg/dL";
      if (barCortisol) {
        barCortisol.style.width = isAlert ? "92%" : "18%";
        barCortisol.className = "bmt-bar " + (isAlert ? "alert" : "calm");
      }
      if (subCortisol) subCortisol.textContent = isAlert ? "Nivel Crítico • Toxicidad Suprarrenal" : "Nivel Basal • Reparación Endocrina";

      const valHrv = document.getElementById("bm-val-hrv");
      const barHrv = document.getElementById("bm-bar-hrv");
      const subHrv = document.getElementById("bm-sub-hrv");
      if (valHrv) valHrv.textContent = isAlert ? "21 ms" : "68 ms";
      if (barHrv) {
        barHrv.style.width = isAlert ? "25%" : "85%";
        barHrv.className = "bmt-bar " + (isAlert ? "alert" : "calm");
      }
      if (subHrv) subHrv.textContent = isAlert ? "Colapso Autónomo • Tono Vagal Mínimo" : "Alta Variabilidad • Tono Parasimpático";

      const valGlinf = document.getElementById("bm-val-glinf");
      const barGlinf = document.getElementById("bm-bar-glinf");
      const subGlinf = document.getElementById("bm-sub-glinf");
      if (valGlinf) valGlinf.textContent = isAlert ? "0% BLOQUEADO" : "98% ACTIVO";
      if (barGlinf) {
        barGlinf.style.width = isAlert ? "4%" : "98%";
        barGlinf.className = "bmt-bar " + (isAlert ? "alert" : "calm");
      }
      if (subGlinf) subGlinf.textContent = isAlert ? "Adenosina Estancada • Toxicidad Celular" : "Depuración Cerebral de Adenosina";

      const valRisk = document.getElementById("bm-val-risk");
      const barRisk = document.getElementById("bm-bar-risk");
      const subRisk = document.getElementById("bm-sub-risk");
      if (valRisk) valRisk.textContent = isAlert ? "15.0x PELIGRO" : "0.0x SEGURO";
      if (barRisk) {
        barRisk.style.width = isAlert ? "95%" : "4%";
        barRisk.className = "bmt-bar " + (isAlert ? "alert" : "calm");
      }
      if (subRisk) subRisk.textContent = isAlert ? "Probabilidad Crítica de Microsueño" : "Reflejos y Frenado al 100%";

      // Narración SomniBot condicional
      if (playVoice) {
        if (isAlert) {
          speakSomniBot("En sobrecarga por estrés, la amígdala secuestra el control, el cortisol satura el cerebro y el riesgo de microsueño se multiplica por quince.");
        } else {
          speakSomniBot("En descompresión y recuperación biológica, el cortisol desciende a niveles basales, el sistema glinfático limpia los residuos de la corteza y tus reflejos psicomotores se restauran al cien por ciento para un turno seguro.", null, "stress_calm");
        }
      }
    }

    function selectBioHotspot(organ) {
      const bafTag = document.getElementById("baf-organ-tag");
      const bafDesc = document.getElementById("baf-organ-desc");

      if (organ === "amygdala") {
        if (bafTag) bafTag.textContent = "ANATOMÍA • AMÍGDALA CEREBRAL (NÚCLEO LÍMBICO)";
        if (bafDesc) bafDesc.textContent = "Estructura subcortical de alarma. Al detectar sobrecarga o estrés laboral, anula el freno racional de la corteza prefrontal y dispara la secreción de cortisol.";
        speakSomniBot("La amígdala es el centro de alarma emocional. En estrés, bloquea la conciliación del sueño.");
      } else if (organ === "vagus") {
        if (bafTag) bafTag.textContent = "ANATOMÍA • NERVIO VAGO (PAR CRANEAL X)";
        if (bafDesc) bafDesc.textContent = "Conecta el tronco encefálico con el corazón y diafragma. La exhalación prolongada del método 4-7-8 lo activa, reduciendo el pulso cardíaco en menos de 60 segundos.";
        speakSomniBot("El nervio vago es el freno biológico de tu cuerpo. Al exhalar largo, desacelera los latidos.");
      }
    }

    document.getElementById("btn-stress-mode-alert").addEventListener("click", () => setStressMode("alert"));
    document.getElementById("btn-stress-mode-calm").addEventListener("click", () => setStressMode("calm"));

    /* =========================================================================
       9. MOTOR DE AUDIO HÍBRIDO: VOZ COLOMBIANA DE MUJER (es-CO-SalomeNeural EN ESTUDIO)
       Garantiza voz femenina humana 100% colombiana en Chrome, Edge, Safari y Móviles
       ========================================================================= */
    const SALOME_AUDIO_MAP = {
      // Recorrido Guiado del Cerebro (Fase 0)
      "welcome_auto_tour": "audio/welcome_auto_tour.mp3",
      "brain_tour_1": "audio/brain_tour_1.mp3",
      "brain_tour_2": "audio/brain_tour_2.mp3",
      "brain_tour_3": "audio/brain_tour_3.mp3",
      "brain_tour_4": "audio/brain_tour_4.mp3",
      "brain_tour_4_trans": "audio/brain_tour_4_trans.mp3",

      // Protocolo de Respiración 4-7-8 (Fase 1)
      "resp_intro": "audio/resp_intro.mp3",
      "resp_intro_auto": "audio/resp_intro_auto.mp3",
      "resp_inhale_1": "audio/resp_inhale_1.mp3",
      "resp_inhale_2": "audio/resp_cycle2_inhale.mp3",
      "resp_inhale_3": "audio/resp_cycle3_inhale.mp3",
      "resp_inhale_4": "audio/resp_cycle4_inhale.mp3",
      "resp_hold": "audio/resp_hold.mp3",
      "resp_exhale": "audio/resp_exhale.mp3",
      "resp_resume": "audio/resp_resume.mp3",
      "resp_to_sim_trans": "audio/resp_to_sim_trans.mp3",

      // Simulador de Conducción en Carretera (Fase 2)
      "sim_driving": "audio/sim_driving.mp3",
      "sim_alert": "audio/sim_alert.mp3",
      "sim_crash": "audio/sim_crash.mp3",
      "sim_restart": "audio/sim_restart.mp3",

      // Dilemas de Turno (Fase 3)
      "stage3_intro": "audio/stage3_intro.mp3",
      "dilemma_ok": "audio/dilemma_ok.mp3",
      "dilemma_bad": "audio/dilemma_bad.mp3",

      // Fisiología del Estrés (Fase 4)
      "stage4_intro": "audio/stage4_intro.mp3",
      "stress_alert": "audio/stress_alert.mp3",
      "stress_calm": "audio/stress_calm.mp3",
      "hotspot_amygdala": "audio/hotspot_amygdala.mp3",
      "hotspot_vagus": "audio/hotspot_vagus.mp3",

      // Introducción General y Certificado
      "welcome_intro": "audio/welcome_intro.mp3",
      "cert_completed": "audio/cert_completed.mp3"
    };

    // DURACIONES REALES EXACTAS EN MILISEGUNDOS MEDIDAS DESDE LOS ARCHIVOS MP3
    const SALOME_AUDIO_DURATIONS = {
      "welcome_auto_tour": 10200,
      "brain_tour_1": 7300,
      "brain_tour_2": 7600,
      "brain_tour_3": 7900,
      "brain_tour_4": 9900,
      "brain_tour_4_trans": 18700,
      "resp_intro": 11400,
      "resp_intro_auto": 13850,
      "resp_inhale_1": 2700,
      "resp_inhale_2": 3100,
      "resp_inhale_3": 3100,
      "resp_inhale_4": 3100,
      "resp_hold": 4200,
      "resp_exhale": 3600,
      "resp_resume": 3100,
      "resp_to_sim_trans": 16300,
      "sim_driving": 8100,
      "sim_alert": 9200,
      "sim_crash": 6900,
      "sim_restart": 7200,
      "stage3_intro": 9600,
      "dilemma_ok": 7300,
      "dilemma_bad": 6600,
      "stage4_intro": 10400,
      "stress_alert": 9700,
      "stress_calm": 14000,
      "hotspot_amygdala": 7800,
      "hotspot_vagus": 8100,
      "welcome_intro": 8700,
      "cert_completed": 7100
    };

    let audioCtx = null;
    let colombianVoice = null;
    let isVoiceActive = true;
    let currentAudioPlaybackToken = 0;
    let breathingAutoStartTimer = null;
    let breathingTransitionTimer = null;
    let safeCompleteTimeout = null;
    let activeNoiseSource = null;

    // UNICO REPRODUCTOR MAESTRO HTML5 (Garantiza cero sobreposición de audio en toda la aplicación)
    const masterAudioPlayer = new Audio();
    masterAudioPlayer.preload = "auto";

    function getAudioContext() {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === "suspended") {
        audioCtx.resume();
      }
      return audioCtx;
    }

    window.addEventListener("click", () => getAudioContext(), { once: true });
    window.addEventListener("touchstart", () => getAudioContext(), { once: true });
    window.addEventListener("keydown", () => getAudioContext(), { once: true });

    function stopAllSomniAudio() {
      currentAudioPlaybackToken++;

      if (safeCompleteTimeout) {
        clearTimeout(safeCompleteTimeout);
        safeCompleteTimeout = null;
      }

      // 1. Inmediata detención del reproductor maestro
      try {
        masterAudioPlayer.pause();
        masterAudioPlayer.currentTime = 0;
        masterAudioPlayer.onended = null;
        masterAudioPlayer.onerror = null;
        masterAudioPlayer.onpause = null;
        masterAudioPlayer.src = "";
      } catch(e) {}

      // 2. Detención de ruido Web Audio (inhalación/exhalación)
      if (activeNoiseSource) {
        try { activeNoiseSource.stop(); } catch(e) {}
        activeNoiseSource = null;
      }

      // 3. Cancelación forzosa de Web Speech API (síntesis de voz del navegador)
      if ("speechSynthesis" in window) {
        try { window.speechSynthesis.cancel(); } catch(e) {}
      }

      const eq = document.getElementById("somnibot-eq-indicator");
      if (eq) eq.classList.remove("is-speaking");
    }

    function detectVoices() {
      if (!("speechSynthesis" in window)) return;
      const voices = window.speechSynthesis.getVoices();
      if (!voices || voices.length === 0) return;

      colombianVoice = voices.find(v => (v.name.includes("Salome") || (v.lang === "es-CO" && v.name.includes("Natural"))))
        || voices.find(v => (v.lang === "es-CO" || v.name.includes("Colombia")) && !v.name.includes("Desktop") && !v.name.includes("Raul"))
        || voices.find(v => v.name.includes("Natural") && (v.lang === "es-MX" || v.lang === "es-US" || v.lang.startsWith("es")))
        || voices.find(v => v.name.includes("Google") && (v.lang === "es-US" || v.lang === "es-419" || v.lang.startsWith("es")))
        || voices.find(v => !v.localService && v.lang.startsWith("es"))
        || voices.find(v => v.lang.startsWith("es"))
        || null;
    }

    if ("speechSynthesis" in window) {
      window.speechSynthesis.onvoiceschanged = detectVoices;
      detectVoices();
      setTimeout(detectVoices, 250);
      setTimeout(detectVoices, 1000);
    }

    function fallbackWebSpeech(text, onComplete) {
      if (!text || !isVoiceActive || !("speechSynthesis" in window)) {
        const eq = document.getElementById("somnibot-eq-indicator");
        if (eq) eq.classList.remove("is-speaking");
        if (onComplete) onComplete();
        return;
      }

      // Incondicional detención de cualquier audio previo antes de síntesis
      stopAllSomniAudio();

      const thisToken = ++currentAudioPlaybackToken;
      const thisStage = currentStageIndex;
      const eq = document.getElementById("somnibot-eq-indicator");
      if (eq) eq.classList.add("is-speaking");

      if (!colombianVoice) detectVoices();

      const plainText = text.replace(/<[^>]*>?/gm, "");
      const utterance = new SpeechSynthesisUtterance(plainText);

      if (colombianVoice) {
        utterance.voice = colombianVoice;
        utterance.lang = colombianVoice.lang;
      } else {
        utterance.lang = "es-CO";
      }

      utterance.rate = 0.94;
      utterance.pitch = 1.0;
      utterance.volume = 1.0;

      utterance.onend = () => {
        if (thisToken === currentAudioPlaybackToken && currentStageIndex === thisStage) {
          if (eq) eq.classList.remove("is-speaking");
          if (onComplete) onComplete();
        }
      };
      utterance.onerror = () => {
        if (thisToken === currentAudioPlaybackToken && currentStageIndex === thisStage) {
          if (eq) eq.classList.remove("is-speaking");
          if (onComplete) onComplete();
        }
      };

      setTimeout(() => {
        if (thisToken === currentAudioPlaybackToken && currentStageIndex === thisStage) {
          try { window.speechSynthesis.speak(utterance); } catch (e) {
            if (eq) eq.classList.remove("is-speaking");
          }
        }
      }, 50);
    }

    function playSalomeAudio(audioKey, displayText, onComplete) {
      const speechBox = document.getElementById("somnibot-text-target");
      if (speechBox && displayText) speechBox.innerHTML = displayText;

      const eq = document.getElementById("somnibot-eq-indicator");

      // Detener cualquier audio o timer previo de inmediato
      stopAllSomniAudio();

      const thisToken = ++currentAudioPlaybackToken;
      const thisStage = currentStageIndex;

      let hasCompleted = false;
      const safeComplete = () => {
        if (hasCompleted) return;
        hasCompleted = true;
        if (safeCompleteTimeout) {
          clearTimeout(safeCompleteTimeout);
          safeCompleteTimeout = null;
        }
        if (thisToken === currentAudioPlaybackToken && currentStageIndex === thisStage) {
          if (eq) eq.classList.remove("is-speaking");
          if (onComplete) onComplete();
        }
      };

      const exactDuration = (typeof SALOME_AUDIO_DURATIONS !== "undefined" && SALOME_AUDIO_DURATIONS[audioKey])
        ? SALOME_AUDIO_DURATIONS[audioKey]
        : Math.max(3500, (displayText ? displayText.split(" ").length * 350 : 3500));

      if (!isVoiceActive) {
        if (eq) eq.classList.remove("is-speaking");
        safeCompleteTimeout = setTimeout(safeComplete, exactDuration);
        return;
      }

      const audioSrc = SALOME_AUDIO_MAP[audioKey];
      if (audioSrc) {
        masterAudioPlayer.src = audioSrc;
        if (eq) eq.classList.add("is-speaking");

        masterAudioPlayer.onended = () => {
          safeComplete();
        };

        masterAudioPlayer.onerror = () => {
          safeCompleteTimeout = setTimeout(safeComplete, exactDuration);
        };

        // Temporizador de respaldo exacto (solo si el audio está pausado/bloqueado)
        safeCompleteTimeout = setTimeout(() => {
          if (!hasCompleted && (masterAudioPlayer.paused || masterAudioPlayer.ended || masterAudioPlayer.readyState === 0)) {
            safeComplete();
          }
        }, exactDuration + 600);

        masterAudioPlayer.play().catch(err => {
          console.warn("Autoplay bloqueado. La progresión continúa con temporizador:", err);
          safeCompleteTimeout = setTimeout(safeComplete, exactDuration);
        });
      } else {
        safeCompleteTimeout = setTimeout(safeComplete, exactDuration);
      }
    }

    function matchSalomeAudioKey(text) {
      if (!text) return null;
      if (text.includes("descompresión diafragmática") || text.includes("tres ciclos del protocolo") || text.includes("simulador de conducción")) return "resp_to_sim_trans";
      if (text.includes("calmar el cerebro") || text.includes("calmamos el cerebro") || text.includes("Bienvenido al protocolo 4-7-8") || text.includes("técnica diafragmática") || text.includes("estimula el nervio vago")) return "resp_intro";
      if (text.includes("Inhala profundamente por la nariz") || text.includes("Inhala suavemente")) return "resp_inhale_1";
      if (text.includes("Retén el aire con calma") || text.includes("mantén el diafragma")) return "resp_hold";
      if (text.includes("Exhala lentamente por la boca") || text.includes("liberando la tensión")) return "resp_exhale";
      if (text.includes("Alerta de fatiga crítica")) return "sim_alert";
      if (text.includes("Microsueño total") || text.includes("perdido el control")) return "sim_crash";
      if (text.includes("Estás al volante en la autopista")) return "sim_driving";
      if (text.includes("Simulador reiniciado")) return "sim_restart";
      if (text.includes("Excelente decisión")) return "dilemma_ok";
      if (text.includes("Atención: este hábito")) return "dilemma_bad";
      if (text.includes("sobrecarga por estrés")) return "stress_alert";
      if (text.includes("recuperación biológica") || text.includes("descompresión y recuperación") || text.includes("descompresión vagal")) return "stress_calm";
      if (text.includes("amígdala es el centro")) return "hotspot_amygdala";
      if (text.includes("nervio vago es el freno")) return "hotspot_vagus";
      if (text.includes("Bienvenido a tu entrenamiento interactivo")) return "welcome_intro";
      if (text.includes("Evalúa cada decisión operativa")) return "stage3_intro";
      if (text.includes("biocircuito neurobiológico") || text.includes("Diagrama del biocircuito")) return "stage4_intro";
      if (text.includes("Felicitaciones. Has completado el recorrido")) return "cert_completed";
      return null;
    }

    function speakSomniBot(text, onComplete, explicitKey) {
      const speechBox = document.getElementById("somnibot-text-target");
      if (speechBox) speechBox.innerHTML = text;

      const key = explicitKey || matchSalomeAudioKey(text);
      if (key && SALOME_AUDIO_MAP[key]) {
        playSalomeAudio(key, text, onComplete);
      } else {
        fallbackWebSpeech(text, onComplete);
      }
    }

    document.getElementById("btn-toggle-voice").addEventListener("click", () => {
      isVoiceActive = !isVoiceActive;
      const label = document.getElementById("label-voice-status");
      if (label) label.textContent = isVoiceActive ? "Voz: Salomé (Colombia)" : "Voz Silenciada";
      const btn = document.getElementById("btn-toggle-voice");
      if (btn) btn.classList.toggle("is-muted", !isVoiceActive);
      if (!isVoiceActive) {
        stopAllSomniAudio();
      }
    });

    document.getElementById("somnibot-trigger").addEventListener("click", () => {
      const speechBox = document.getElementById("somnibot-text-target");
      if (speechBox) speakSomniBot(speechBox.textContent);
    });

    function playInhaleSound() {
      try {
        const ctx = getAudioContext();
        const bufferSize = Math.floor(ctx.sampleRate * 4.0);
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) data[i] = Math.random() * 2 - 1;

        const noise = ctx.createBufferSource();
        noise.buffer = buffer;
        const filter = ctx.createBiquadFilter();
        filter.type = "bandpass";
        filter.Q.value = 3.2;
        filter.frequency.setValueAtTime(240, ctx.currentTime);
        filter.frequency.exponentialRampToValueAtTime(780, ctx.currentTime + 4.0);

        if (activeNoiseSource) {
          try { activeNoiseSource.stop(); } catch(e) {}
          activeNoiseSource = null;
        }

        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.001, ctx.currentTime);
        gain.gain.linearRampToValueAtTime(0.035, ctx.currentTime + 2.0);
        gain.gain.linearRampToValueAtTime(0.001, ctx.currentTime + 4.0);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        activeNoiseSource = noise;
        noise.start();
      } catch (e) {}
    }

    function playExhaleSound() {
      try {
        const ctx = getAudioContext();
        const bufferSize = Math.floor(ctx.sampleRate * 8.0);
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) data[i] = Math.random() * 2 - 1;

        const noise = ctx.createBufferSource();
        noise.buffer = buffer;
        const filter = ctx.createBiquadFilter();
        filter.type = "lowpass";
        filter.frequency.setValueAtTime(700, ctx.currentTime);
        filter.frequency.exponentialRampToValueAtTime(160, ctx.currentTime + 8.0);

        if (activeNoiseSource) {
          try { activeNoiseSource.stop(); } catch(e) {}
          activeNoiseSource = null;
        }

        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.001, ctx.currentTime);
        gain.gain.linearRampToValueAtTime(0.030, ctx.currentTime + 2.0);
        gain.gain.linearRampToValueAtTime(0.001, ctx.currentTime + 8.0);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        activeNoiseSource = noise;
        noise.start();
      } catch (e) {}
    }

    function playScreechAndCrashSound() {
      try {
        const ctx = getAudioContext();
        const osc = ctx.createOscillator();
        const oscGain = ctx.createGain();
        osc.type = "sawtooth";
        osc.frequency.setValueAtTime(950, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(220, ctx.currentTime + 1.2);
        oscGain.gain.setValueAtTime(0.18, ctx.currentTime);
        oscGain.gain.linearRampToValueAtTime(0.001, ctx.currentTime + 1.2);
        osc.connect(oscGain);
        oscGain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 1.3);

        const bufferSize = Math.floor(ctx.sampleRate * 1.5);
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
          data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (ctx.sampleRate * 0.3));
        }
        const noise = ctx.createBufferSource();
        noise.buffer = buffer;
        const filter = ctx.createBiquadFilter();
        filter.type = "highpass";
        filter.frequency.setValueAtTime(1200, ctx.currentTime);
        const noiseGain = ctx.createGain();
        noiseGain.gain.setValueAtTime(0.25, ctx.currentTime);
        noiseGain.gain.linearRampToValueAtTime(0.001, ctx.currentTime + 1.4);
        noise.connect(filter);
        filter.connect(noiseGain);
        noiseGain.connect(ctx.destination);
        noise.start();
      } catch (e) {}
    }

    /* =========================================================================
       10. CONTROLADOR DE FASES
       ========================================================================= */
    function goToStage(index) {
      // 1. Inmediata e incondicional cancelación de cualquier audio y timer activo de la fase previa
      stopAllSomniAudio();

      // Limpiar incondicionalmente todos los timers de transición y animación
      if (brainTourTimer) {
        clearTimeout(brainTourTimer);
        brainTourTimer = null;
      }
      if (breathingAutoStartTimer) {
        clearTimeout(breathingAutoStartTimer);
        breathingAutoStartTimer = null;
      }
      if (breathingTransitionTimer) {
        clearTimeout(breathingTransitionTimer);
        breathingTransitionTimer = null;
      }
      if (drivingAutoTimer) {
        clearInterval(drivingAutoTimer);
        drivingAutoTimer = null;
      }
      if (fatigueTimer) {
        clearInterval(fatigueTimer);
        fatigueTimer = null;
      }
      if (crashTransTimer) {
        clearInterval(crashTransTimer);
        crashTransTimer = null;
      }
      if (safeCompleteTimeout) {
        clearTimeout(safeCompleteTimeout);
        safeCompleteTimeout = null;
      }

      // 2. Detener estados y bucles específicos de la fase anterior
      if (currentStageIndex === 0) {
        isBrainTourPlaying = false;
        updateTourPlayPauseBtnUI();
      } else if (currentStageIndex === 1) {
        isBreathingActive = false;
        isBreathingIntro = false;
        const labelToggle = document.getElementById("label-toggle-breath");
        if (labelToggle) labelToggle.textContent = "Comenzar Ejercicio Guiado";
      } else if (currentStageIndex === 2) {
        isDrivingFull = false;
      }

      currentStageIndex = index;

      stageLayers.forEach((layer, idx) => {
        layer.classList.toggle("is-active", idx === index);
      });

      stagePills.forEach((pill, idx) => {
        pill.classList.toggle("is-active", idx === index);
      });

      if (dockStageIndicator) {
        dockStageIndicator.textContent = stageTitles[index] || `ETAPA ${index + 1} DE 5`;
      }

      requestAnimationFrame(resizeAllCanvases);

      // Resetear scroll al cambiar de etapa en móvil / pantalla dividida
      const mainViewport = document.querySelector(".main-stages-viewport");
      if (mainViewport) mainViewport.scrollTop = 0;

      // Auto-centrar la píldora activa en la barra horizontal móvil
      const activePill = stagePills[index];
      if (activePill && activePill.scrollIntoView) {
        activePill.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
      }

      if (index === 0) {
        setBrainStateGlobal("calm");
        speakSomniBot("Bienvenido a tu entrenamiento interactivo. Rota el cerebro en 3D para examinar cómo el descanso repara tus conexiones o activa el recorrido guiado.", null, "welcome_intro");
      } else if (index === 1) {
        setBreathingIntroState(true);
      } else if (index === 2) {
        startDrivingSimulatorStage();
      } else if (index === 3) {
        renderDilemma(0, false); // false para evitar duplicar locución con stage3_intro
        speakSomniBot("Evalúa cada decisión operativa. Observa cómo tus elecciones impactan en tiempo real el equilibrio o la sobrecarga de tu corteza cerebral.", null, "stage3_intro");
      } else if (index === 4) {
        setStressMode("alert", false); // false para evitar duplicar locución con stage4_intro
        speakSomniBot("Diagrama del biocircuito neurobiológico: observa cómo la sobrecarga operativa colapsa tus reflejos y cómo el descanso reparador restablece el equilibrio de tu organismo.", null, "stage4_intro");
      }
    }

    stagePills.forEach(pill => {
      pill.addEventListener("click", () => {
        goToStage(parseInt(pill.dataset.stage, 10));
      });
    });

    document.getElementById("btn-dock-global-prev").addEventListener("click", () => {
      if (currentStageIndex > 0) goToStage(currentStageIndex - 1);
    });

    document.getElementById("btn-dock-global-next").addEventListener("click", () => {
      if (currentStageIndex < 4) goToStage(currentStageIndex + 1);
    });

    document.getElementById("btn-start-exp-breath").addEventListener("click", () => {
      goToStage(1);
    });

    /* =========================================================================
       11. REDIMENSIONAMIENTO DE LIENZOS
       ========================================================================= */
    function resizeAllCanvases() {
      if (bgCanvas) {
        bgCanvas.width = window.innerWidth;
        bgCanvas.height = window.innerHeight;
      }
      if (brainCanvas) {
        const p = brainCanvas.parentElement;
        brainCanvas.width = (p && p.clientWidth > 50) ? p.clientWidth : 800;
        brainCanvas.height = (p && p.clientHeight > 50) ? p.clientHeight : 560;
      }
      if (breathCanvas) {
        const p = breathCanvas.parentElement;
        breathCanvas.width = (p && p.clientWidth > 50) ? p.clientWidth : 750;
        breathCanvas.height = (p && p.clientHeight > 50) ? p.clientHeight : 520;
      }
      if (truckFullCanvas) {
        const stageEl = document.getElementById("stage-truck-full");
        const p = truckFullCanvas.parentElement;
        truckFullCanvas.width = (stageEl && stageEl.clientWidth > 50) ? stageEl.clientWidth : (p && p.clientWidth > 50 ? p.clientWidth : (window.innerWidth - 48));
        truckFullCanvas.height = (stageEl && stageEl.clientHeight > 50) ? stageEl.clientHeight : (p && p.clientHeight > 50 ? p.clientHeight : (window.innerHeight - 170));
      }
      if (dilemmaBrainCanvas) {
        const p = dilemmaBrainCanvas.parentElement;
        dilemmaBrainCanvas.width = (p && p.clientWidth > 50) ? p.clientWidth : 380;
        dilemmaBrainCanvas.height = (p && p.clientHeight > 50) ? p.clientHeight : 280;
      }
    }

    window.addEventListener("orientationchange", () => {
      setTimeout(() => {
        resizeAllCanvases();
        initBgParticles();
      }, 200);
    });

    window.addEventListener("resize", () => {
      resizeAllCanvases();
      initBgParticles();
    });

    resizeAllCanvases();
    requestAnimationFrame(render3DInteractiveBrain);
    requestAnimationFrame(renderHolographicLungs);
    requestAnimationFrame(renderProceduralHighwaySimulator);
    requestAnimationFrame(renderDilemmaBrain);

    /* =========================================================================
       12. INICIO AUTOMÁTICO DE LA EXPERIENCIA: BIENVENIDA Y RUTA GUIADA 3D
       ========================================================================= */
    let initialAutoExperienceStarted = false;

    function startInitialAutoExperience() {
      if (initialAutoExperienceStarted) return;
      initialAutoExperienceStarted = true;

      isBrainTourPlaying = true;
      updateTourPlayPauseBtnUI();

      const welcomeText = "Bienvenido a tu entrenamiento interactivo en higiene del sueño y alerta operativa de ISAVAL SG-SST. Iniciamos el recorrido guiado por tu neurobiología.";

      playSalomeAudio("welcome_auto_tour", welcomeText, () => {
        if (isBrainTourPlaying && currentStageIndex === 0) {
          brainTourTimer = setTimeout(() => {
            if (isBrainTourPlaying && currentStageIndex === 0) {
              setBrainTourStep(1, false);
            }
          }, 400);
        }
      });
    }

    // Iniciar automáticamente tras la carga del DOM
    setTimeout(() => {
      startInitialAutoExperience();
    }, 300);

    // Desbloqueo transparente de audio al primer clic o toque en cualquier parte
    const unlockUserAudio = () => {
      if (audioCtx && audioCtx.state === "suspended") {
        audioCtx.resume();
      }
      if (isVoiceActive && masterAudioPlayer.src && masterAudioPlayer.paused && !masterAudioPlayer.ended) {
        masterAudioPlayer.play().catch(() => {});
      }
    };
    window.addEventListener("click", unlockUserAudio, { passive: true });
    window.addEventListener("touchstart", unlockUserAudio, { passive: true });
    window.addEventListener("keydown", unlockUserAudio, { passive: true });

  </script>
</body>
</html>
'''

with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print("Master V9 generated successfully into:", target_path)
