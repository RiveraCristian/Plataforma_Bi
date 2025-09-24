export interface MetricConfig {
  id: number;
  name: string;
  expression: string;
}

export interface DashboardWidget {
  id: string;
  datasetId: number;
  metrics: MetricConfig[];
  configuration: Record<string, unknown>;
}

export interface DashboardDefinition {
  id: number;
  name: string;
  owner_id: number;
  layout_json: Record<string, unknown>;
  description?: string;
}
