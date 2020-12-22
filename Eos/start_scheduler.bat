@echo off 
dask-scheduler.exe --tls-ca-file certs/myCA.pem --tls-cert certs/scheduler.crt --tls-key certs/scheduler.key --protocol tls
@REM dask-worker.exe --tls-ca-file certs/myCA.pem --tls-cert certs/worker.crt --tls-key certs/worker.key --protocol tls tls://192.168.1.151:8786
echo "The program has completed"