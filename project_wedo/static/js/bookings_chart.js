document.addEventListener("DOMContentLoaded", function () {
  fetch("/admin/bookings/chart-data/") // Ubah sesuai dengan URL yang benar untuk mengambil data chart
    .then((response) => response.json())
    .then((data) => {
      var ctx = document.getElementById("bookingsChart").getContext("2d");
      var bookingsChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.labels,
          datasets: [
            {
              label: "Total Bookings",
              data: data.bookings,
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    });
});
