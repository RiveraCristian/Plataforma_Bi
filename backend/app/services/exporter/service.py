from pathlib import Path

class ExporterService:
    """Generate export files for dashboards."""

    def export_dashboard(self, dashboard_id: int, export_type: str) -> Path:
        if export_type not in {"pdf", "png"}:
            raise ValueError("Unsupported export type")
        export_dir = Path("exports")
        export_dir.mkdir(parents=True, exist_ok=True)
        file_path = export_dir / f"dashboard_{dashboard_id}.{export_type}"
        file_path.write_text(f"Placeholder {export_type.upper()} export for dashboard {dashboard_id}")
        return file_path
