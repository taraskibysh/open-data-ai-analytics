output "public_ip_address" {
  value       = azurerm_public_ip.public_ip.ip_address
  description = "Публічна IP-адреса для доступу до веб-інтерфейсу та SSH"
}