import numpy as np
import pandas as pd # Dodano import pandas

def dodawanie(liczba1, liczba2):
    return np.add(liczba1, liczba2)

def odejmowanie(liczba1, liczba2):
    return np.subtract(liczba1, liczba2)

def mnozenie(liczba1, liczba2):
    return np.multiply(liczba1, liczba2)

def dzielenie(liczba1, liczba2):
    if liczba2 != 0:
        return np.divide(liczba1, liczba2)
    else:
        return "Błąd: dzielenie przez zero!"

# --- NOWE FUNKCJE Z PANDAS ---
def sumuj_kolumne_df(df, nazwa_kolumny):
    """
    Sumuje wartości w określonej kolumnie DataFrame.
    """
    if nazwa_kolumny in df.columns:
        return df[nazwa_kolumny].sum()
    else:
        return "Błąd: Kolumna nie istnieje!"

def srednia_kolumny_df(df, nazwa_kolumny):
    """
    Oblicza średnią wartości w określonej kolumnie DataFrame.
    """
    if nazwa_kolumny in df.columns:
        return df[nazwa_kolumny].mean()
    else:
        return "Błąd: Kolumna nie istnieje!"

def filtruj_df_wg_wartosci(df, nazwa_kolumny, wartosc):
    """
    Filtruje DataFrame na podstawie wartości w określonej kolumnie.
    """
    if nazwa_kolumny in df.columns:
        return df[df[nazwa_kolumny] == wartosc]
    else:
        return pd.DataFrame() # Zwracamy pusty DataFrame w przypadku błędu