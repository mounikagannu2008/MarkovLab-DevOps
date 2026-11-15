
package edu.markovlab;

import java.util.Map;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@RestController
public class GenerationController {

    private final String engineUrl;
    private final RestTemplate restTemplate = new RestTemplate();

    public GenerationController(
            @Value("${ENGINE_URL:http://engine:8000}") String engineUrl) {
        this.engineUrl = engineUrl;
    }

    @PostMapping("/generate")
    public ResponseEntity<Map> generate(
            @RequestBody Map<String, Object> request) {

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<Map<String, Object>> entity =
                new HttpEntity<>(request, headers);

        ResponseEntity<Map> response = restTemplate.exchange(
                engineUrl + "/generate",
                HttpMethod.POST,
                entity,
                Map.class
        );

        return ResponseEntity.ok(response.getBody());
    }
}
