# Sleigh

Sleigh is a simple [Santa](https://github.com/google/santa) server that allows
you to remotely synchronize Santa rulesets across machines.

**WARNING:** Sleigh is currently under heavy development.

## Deployment

The (personally) recommended deployment is using:
- Cloudflare's [API Shield](https://developers.cloudflare.com/firewall/cf-firewall-rules/api-shield).
- A reverse proxy, such as [Nginx](https://nginx.com).
- [Gunicorn](https://gunicorn.org) at the core, with the passive restart option after X number of requests to avoid any possible memory leaks.

Nginx and Gunicorn is included in the Sleigh Docker container: ghcr.io/andre4ik3/sleigh
