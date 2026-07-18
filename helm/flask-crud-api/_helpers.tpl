{{/*
Expand the name of the chart.
*/}}

{{- define "flask.name" -}}
{{- default .Chart.Name .Values.nameOverride }}
{{- end }}

{{/*
Create fullname.
*/}}

{{- define "flask.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride }}
{{- else }}
{{- printf "%s-%s" .Release.Name (include "flask.name" .) }}
{{- end }}
{{- end }}

{{/*
Labels
*/}}

{{- define "flask.labels" -}}
app.kubernetes.io/name: {{ include "flask.name" . }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
