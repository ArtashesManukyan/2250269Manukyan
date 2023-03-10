from typing import Union
import numpy as np
import pandas as pd
import h5py

# generates paths, assignes them to "pfade" array and returns the "pfade" array.
def gen_path_for_multi_speeds(
    run_id: int, index: list[str], pump_speeds: list[float]
) -> list[str]:
    
    pfade = []
    for i in index :
        for j in pump_speeds :
            path = '/run' + str(run_id) + '/Kennlinie_ESP_c_' + j + '_' + i
            pfade.append(path)
    return pfade
    pass

# opens hdf5 file as store, gets attributes by key in "att_key", decodes it in "utf-8" format and returnes metadata (if there are no any attributes it prints error message).
def read_dataframe_metadata(
    file: str, path: str, att_key: str
) -> Union[np.float64, np.int32, np.bytes_, None]:
    
    with pd.HDFStore(file, "r") as store:      
        try: 
            return store.get_storer(path).attrs[att_key].decode('utf-8')
        except KeyError: 
            print("Keine Attributes gefunden")
    pass

#opens hdf5 file, checks if value of "key" is equal to passed "att_key" and if it is, returns attributes decoded in "utf-8" format.
def read_group_metadata(
    file: str, path: str, att_key: str
) -> Union[np.float64, np.int32, np.bytes_, None]:
    
    hdf = h5py.file(file,'r')[path]
    for key in hdf.attrs.keys():
        if key == att_key:
            return hdf.attrs[key].decode('utf-8')
    pass


def get_df(file: str, path: str) -> pd.DataFrame:
    pass


def check_col_signum(df: pd.DataFrame, col: str, threshold: int) -> None:
    pass


def check_number_of_measurements(
    df: pd.DataFrame, col: str, f: float, t: float
) -> None:
    pass


def gen_plotdata(
    file_path: str,
    path_list: list,
    cols: list,
    output_size: tuple,
) -> np.ndarray:
    pass


def get_average_value(df: pd.DataFrame, col: str) -> float:
    pass


def get_std_deviation(df: pd.DataFrame, col: str) -> float:
    pass


def std_uniform_to_normal(std_uniform: float) -> float:
    pass


def total_uncertainty(stat: float, sys: float) -> float:
    pass


def convert_bar_to_pa(v: pd.Series) -> pd.Series:
    pass


def convert_lpm_to_qmps(v: pd.Series) -> pd.Series:
    pass


def dataframe_dedimension(
    plot_data: pd.DataFrame,
    pump_speeds: list,
    metadata: dict,
) -> pd.DataFrame:
    pass


def convert_rpm_to_hz(v: float) -> float:
    pass


def calc_pressure_number(
    delta_p: float,
    n: float,
    d: float,
    rho: float,
) -> float:
    pass


def calc_flow_number(q: float, n: float, d: float) -> float:
    pass


def uncertainty_pressure_number(
    total_uncertainty_p: float,
    p: float,
    total_uncertainty_rho: float,
    rho: float,
    total_uncertainty_n: float,
    n: float,
    total_uncertainty_d: float,
    d: float,
    psi: float,
) -> float:
    pass


def uncertainty_flow_number(
    total_uncertainty_q: float,
    q: float,
    total_uncertainty_n: float,
    n: float,
    total_uncertainty_d: float,
    d: float,
    phi: float,
) -> float:
    pass


def main():
    # DEBUG und Test
    pass


if __name__ == "__main__":
    main()
