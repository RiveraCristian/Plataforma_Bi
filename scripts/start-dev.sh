#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"

log() {
  echo "[start-dev] $1"
}

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "[start-dev] ERROR: Se requiere el comando '$1' en el PATH." >&2
    exit 1
  fi
}

log "Verificando dependencias..."
require_cmd poetry
require_cmd yarn

log "Instalando dependencias del backend (si es necesario)..."
(
  cd "$BACKEND_DIR"
  poetry install --no-interaction --quiet
)

log "Instalando dependencias del frontend (si es necesario)..."
(
  cd "$FRONTEND_DIR"
  yarn install --silent
)

backend_cmd=(poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000)
frontend_cmd=(yarn dev --host 0.0.0.0 --port 5173)

pids=()

cleanup() {
  log "Deteniendo servicios..."
  for pid in "${pids[@]}"; do
    if kill -0 "$pid" >/dev/null 2>&1; then
      kill "$pid" >/dev/null 2>&1 || true
      wait "$pid" 2>/dev/null || true
    fi
  done
}

trap cleanup EXIT INT TERM

log "Iniciando backend en http://localhost:8000 ..."
(
  cd "$BACKEND_DIR"
  "${backend_cmd[@]}"
) &
pids+=($!)

log "Iniciando frontend en http://localhost:5173 ..."
(
  cd "$FRONTEND_DIR"
  "${frontend_cmd[@]}"
) &
pids+=($!)

log "Servicios en ejecución. Presiona Ctrl+C para detener."

for pid in "${pids[@]}"; do
  wait "$pid"
done
