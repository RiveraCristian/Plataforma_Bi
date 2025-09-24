import axios from "axios";

const apiClient = axios.create({
  baseURL: "/api",
  timeout: 10000
});

export async function fetchDashboards() {
  const response = await apiClient.get("/catalog/dashboards");
  return response.data;
}

export async function executeQuery(params: { datasetId: number; metricIds: number[]; dimensions?: string[] }) {
  const response = await apiClient.post("/query/execute", {
    dataset_id: params.datasetId,
    metric_ids: params.metricIds,
    dimensions: params.dimensions
  });
  return response.data;
}
