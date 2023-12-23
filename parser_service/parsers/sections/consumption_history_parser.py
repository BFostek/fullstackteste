from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class Consumption:
    # 'MÊS/ANO', 'Cons. kWh', 'Média kWh/Dia', 'Dias',
    date: str
    total_consumption: int
    mean_consumption: str
    total_days: int


def split_consumption_data(sliced_list, elements_per_list):
    return [sliced_list[i:i + elements_per_list] for i in range(0, len(sliced_list), elements_per_list)]


class ConsumptionHistoryParser:
    @staticmethod
    def get_index(data, marker, offset=0):
        try:
            return data.index(marker) + offset
        except ValueError:
            raise Exception("Marker not found in data")

    @staticmethod
    def parse(data):
        start_marker = "Histórico de Consumo"
        end_marker = "Reservado ao Fisco"
        initial_index = ConsumptionHistoryParser.get_index(data, start_marker, 5)
        final_index = ConsumptionHistoryParser.get_index(data, end_marker)

        consumption_slice = data[initial_index:final_index]
        return {"name": "consumptionHistory",
                "content": [Consumption(*consumption)
                            for consumption in split_consumption_data(consumption_slice, 4)]}
