from googleanalytics import Connection, GoogleAnalyticsError

def get_google_analytics_data():
    # Buat objek koneksi ke Google Analytics
    connection = Connection('<YOUR_VIEW_ID>', '<YOUR_SERVICE_ACCOUNT_KEY_FILE_PATH>')

    try:
        # Jalankan permintaan untuk mendapatkan data
        data = connection.get_report(
            start_date='yyyy-mm-dd',
            end_date='yyyy-mm-dd',
            metrics=['ga:sessions', 'ga:users'],
            dimensions=['ga:date']
        )

        # Manipulasi data sesuai kebutuhan Anda
        # Contoh: ambil tanggal dan jumlah sesi
        result = []
        for row in data['rows']:
            date = row[0]
            sessions = row[1]
            result.append({'date': date, 'sessions': sessions})

        return result

    except GoogleAnalyticsError as e:
        # Tangani kesalahan jika terjadi
        print(f"Error retrieving Google Analytics data: {str(e)}")
        return []
