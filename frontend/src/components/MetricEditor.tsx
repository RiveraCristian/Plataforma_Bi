import { Button, Card, NumberInput, Select, Stack, TextInput, Title } from "@mantine/core";

const aggregationOptions = [
  { value: "sum", label: "Suma" },
  { value: "avg", label: "Promedio" },
  { value: "count", label: "Conteo" }
];

function MetricEditor() {
  return (
    <Card withBorder shadow="sm" padding="lg" radius="md" style={{ flex: 1 }}>
      <Title order={3} mb="md">
        Editor de Métricas
      </Title>
      <Stack>
        <TextInput label="Nombre de la métrica" placeholder="Ingresos netos" required />
        <Select label="Campo base" placeholder="Selecciona un campo" data={["monto", "cantidad", "descuento"]} searchable />
        <Select label="Agregación" data={aggregationOptions} placeholder="Selecciona" required />
        <NumberInput label="Factor" placeholder="1" min={0} precision={2} defaultValue={1} />
        <Button variant="filled">Guardar métrica</Button>
      </Stack>
    </Card>
  );
}

export default MetricEditor;
