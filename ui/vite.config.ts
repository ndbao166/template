import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'node:path'

// https://vite.dev/config/
export default defineConfig({
  envDir: path.resolve(__dirname, '..'),
  server: {
    host: '0.0.0.0',
    port: 3000,
    allowedHosts: ["0.0.0.0", "pi.local"],
  },
  plugins: [
    react({
      babel: {
        plugins: [['babel-plugin-react-compiler']],
      },
    }),
  ],
})
