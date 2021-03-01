<h1 align="center">🛷 Sleigh 🛷</h1>
<p align="center">A Santa Synchronization Server</p>

<p align="center">
  <a href="https://github.com/andre4ik3/sleigh/actions/workflows/ci.yml">
    <img src="https://github.com/andre4ik3/sleigh/actions/workflows/ci.yml/badge.svg?branch=community" />
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-black" />
  </a>
</p>

Sleigh is a simple [Santa](https://github.com/google/santa) server that allows
you to remotely synchronize Santa rulesets across machines.

**WARNING:** Sleigh is currently under heavy development.

## Deployment

The (personally) recommended deployment is using:
- Cloudflare's [API Shield](https://developers.cloudflare.com/firewall/cf-firewall-rules/api-shield).
- A reverse proxy, such as [Nginx](https://nginx.com).
- [Gunicorn](https://gunicorn.org) at the core, with the passive restart option after X number of requests to avoid any possible memory leaks.

Nginx and Gunicorn are included in the [Sleigh Docker container](https://github.com/users/andre4ik3/packages/container/package/sleigh)
