library(shiny)
library(ggplot2)
library(dplyr)
#Use CRAN USA MO if you must select one. 

# Sample data
set.seed(123)
data <- data.frame(
  Date = seq(as.Date("2025-01-01"), by = "day", length.out = 30),
  Revenue = round(runif(30, 50, 200), 2)
)

# UI
ui <- fluidPage(
  titlePanel("💡 Shiny App: Revenue Scatter Plot"),

  sidebarLayout(
    sidebarPanel(
      dateRangeInput("date_range", "Select Date Range:",
                     start = min(data$Date), end = max(data$Date))
    ),

    mainPanel(
      splitLayout(
        cellWidths = c("60%", "40%"),
        plotOutput("scatterPlot"),
        tableOutput("summaryTable")
      )
    )
  )
)

# Server
server <- function(input, output) {
  
  filtered_data <- reactive({
    data %>% filter(Date >= input$date_range[1], Date <= input$date_range[2])
  })

  output$scatterPlot <- renderPlot({
    ggplot(filtered_data(), aes(x = Date, y = Revenue)) +
      geom_point(color = "darkgreen", size = 3) +
      labs(title = "Revenue Over Time", x = "Date", y = "Revenue ($)") +
      theme_minimal()
  })

  output$summaryTable <- renderTable({
    df <- filtered_data()
    summary_stats <- data.frame(
      `Total Revenue` = sum(df$Revenue),
      `Average Revenue` = mean(df$Revenue),
      `Max Revenue` = max(df$Revenue),
      `Min Revenue` = min(df$Revenue)
    )
    t(summary_stats)
  }, rownames = TRUE, colnames = FALSE)
}

# Run the app
shinyApp(ui = ui, server = server)


## Open R Terminal 

### shiny::runApp("shiny_example_app.R")