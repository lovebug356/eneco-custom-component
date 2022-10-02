"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    add_entities([EnergyPriceSensor('Energiekost Dagtarief', 0.2627)])


class EnergyPriceSensor(SensorEntity):
    """Representation of a sensor."""

    def __init__(self, name: str, value: float) -> None:
        """Initialize the sensor."""
        self._name = name
        self._state = value

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return 'Energiekost Dagtarief'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return "€/kWh"

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        pass
