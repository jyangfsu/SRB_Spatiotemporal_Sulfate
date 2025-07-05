library(linkET)  
library(ggplot2)

rm(list = ls())

data("varechem", package = "vegan")
data("varespec", package = "vegan")

varechem <- read.csv("varchem.csv")
varespec  <- read.csv("varpca.csv")
  
  
mantel_test(varespec, varechem)

library(dplyr)
library(ggplot2)


#mantel <- mantel_test(varespec, varechem,
#                      spec_select = list(PC1 = 1:1,
#                                         PC2 = 2:2,
#                                         PC3 = 3:3,
#                                         PC4 = 4:4)) %>% 
  
mantel <- read.csv("mantel.csv") %>% 


  mutate(rd = cut(r, breaks = c(-Inf, 0.3, 0.6, Inf),
                  labels = c("< 0.3", "0.3 - 0.6", ">= 0.6")),
         pd = cut(p, breaks = c(-Inf, 0, Inf),
                  labels = c("< 0", ">= 0")))



qcorrplot(correlate(varechem), type = "upper", diag = FALSE) +
  geom_square() +
  geom_couple(aes(colour = pd, size = rd), data = mantel, curvature = 0.1) +
  scale_fill_gradientn(colours = RColorBrewer::brewer.pal(11, "Spectral")) +
  scale_size_manual(values = c(0.5, 1, 2)) +
  scale_colour_manual(values = color_pal(3)) +
  guides(size = guide_legend(title = "|loadings|",
                             override.aes = list(colour = "grey35"), 
                             order = 2),
         colour = guide_legend(title = "Loadings", 
                               override.aes = list(size = 3), 
                               order = 1),
         fill = guide_colorbar(title = "Pearson's r", order = 3))