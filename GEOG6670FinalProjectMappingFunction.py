class ColorRamps(Enum):
    SEISMIC = 'seismic'
    MAGMA = 'magma'
    INFERNO = 'inferno'
    VIRIDIS = 'viridis'
    CIVIDIS = 'cividis'
    RAINBOW = 'rainbow'

class Schemes(Enum):
    NATURAL_BREAKS = 'natural_breaks'
    QUANTILES = 'quantiles'
    EQUAL_INTERVAL = 'equal_interval'

def plot_map_by_column(
        gdf: gpd.GeoDataFrame, 
        column: float, 
        color_ramp: ColorRamps, 
        scheme: Schemes,
        title: str):
    fig, ax = plt.subplots(figsize=(12, 8), facecolor="#1a1a1a")
    plot = gdf.plot(
        ax=ax,
        column=column,
        cmap=color_ramp.value,
        edgecolor="white",
        linewidth=0.3,
        legend=True,
        scheme=scheme.value,
        legend_kwds={
            'labelcolor': 'white',
            "loc": "center left", 
            'frameon': False},
        alpha=0.6
    )
    plt.title(f"{title}", fontsize=16, color="white")
    ax.set_axis_off()