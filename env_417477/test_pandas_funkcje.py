from calculator import sumuj_kolumne_df, srednia_kolumny_df, filtruj_df_wg_wartosci
import pandas as pd
import pytest

@pytest.fixture
def sample_dataframe():
    """
    Fixture dostarczająca przykładowy DataFrame do testów.
    """
    data = {'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': ['X', 'Y', 'X', 'Z', 'Y']}
    return pd.DataFrame(data)

def test_sumuj_kolumne_df_poprawnie(sample_dataframe):
    assert sumuj_kolumne_df(sample_dataframe, 'A') == 15
    assert sumuj_kolumne_df(sample_dataframe, 'B') == 150

def test_sumuj_kolumne_df_brak_kolumny(sample_dataframe):
    assert sumuj_kolumne_df(sample_dataframe, 'D') == "Błąd: Kolumna nie istnieje!"

def test_srednia_kolumny_df_poprawnie(sample_dataframe):
    assert srednia_kolumny_df(sample_dataframe, 'A') == 3.0
    assert srednia_kolumny_df(sample_dataframe, 'B') == 30.0

def test_srednia_kolumny_df_brak_kolumny(sample_dataframe):
    assert srednia_kolumny_df(sample_dataframe, 'D') == "Błąd: Kolumna nie istnieje!"

def test_filtruj_df_wg_wartosci_poprawnie(sample_dataframe):
    filtered_df = filtruj_df_wg_wartosci(sample_dataframe, 'C', 'X')
    assert len(filtered_df) == 2
    assert filtered_df['A'].tolist() == [1, 3]

def test_filtruj_df_wg_wartosci_brak_kolumny(sample_dataframe):
    filtered_df = filtruj_df_wg_wartosci(sample_dataframe, 'D', 'W')
    assert filtered_df.empty