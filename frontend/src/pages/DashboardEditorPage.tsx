import { useMemo } from "react";
import GridLayout, { Layout } from "react-grid-layout";
import { Card, Group, Text, Title } from "@mantine/core";

import Widget from "../components/Widget";

import "react-grid-layout/css/styles.css";
import "react-resizable/css/styles.css";

const initialLayout: Layout[] = [
  { i: "chart-1", x: 0, y: 0, w: 4, h: 4 },
  { i: "chart-2", x: 4, y: 0, w: 4, h: 4 },
  { i: "chart-3", x: 8, y: 0, w: 4, h: 4 }
];

function DashboardEditorPage() {
  const layout = useMemo(() => initialLayout, []);

  return (
    <section>
      <Group justify="space-between" mb="md">
        <Title order={2}>Editor de Dashboard</Title>
        <Text c="dimmed">Arrastra y suelta los widgets para organizar tu dashboard.</Text>
      </Group>
      <Card withBorder shadow="sm" padding="lg">
        <GridLayout
          className="layout"
          layout={layout}
          cols={12}
          rowHeight={30}
          width={1200}
          isDraggable
          isResizable
        >
          {layout.map((item) => (
            <div key={item.i}>
              <Widget title={`Widget ${item.i}`} description="Configura la métrica y el gráfico desde la derecha." />
            </div>
          ))}
        </GridLayout>
      </Card>
    </section>
  );
}

export default DashboardEditorPage;
