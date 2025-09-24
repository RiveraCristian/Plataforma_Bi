import { Card, Checkbox, Divider, Group, NumberInput, Stack, Text, Title } from "@mantine/core";
import { DatePickerInput } from "@mantine/dates";

function FilterPanel() {
  return (
    <Card withBorder shadow="sm" padding="lg" radius="md" style={{ flex: 1 }}>
      <Title order={3} mb="md">
        Filtros
      </Title>
      <Stack gap="lg">
        <div>
          <Text fw={500} mb="xs">
            Categorías
          </Text>
          <Stack gap="xs">
            <Checkbox label="Norte" />
            <Checkbox label="Centro" />
            <Checkbox label="Sur" />
          </Stack>
        </div>
        <Divider label="Rango de fechas" labelPosition="center" />
        <DatePickerInput label="Desde" placeholder="Selecciona fecha" clearable />
        <DatePickerInput label="Hasta" placeholder="Selecciona fecha" clearable />
        <Divider label="Umbral" labelPosition="center" />
        <Group grow>
          <NumberInput label="Mínimo" placeholder="0" min={0} />
          <NumberInput label="Máximo" placeholder="100" min={0} />
        </Group>
      </Stack>
    </Card>
  );
}

export default FilterPanel;
